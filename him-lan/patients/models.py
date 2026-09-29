from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_doctor = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    ward_type = models.CharField(max_length=50, choices=[('General', 'General'), ('ICU', 'ICU'), ('Pediatrics', 'Pediatrics'), ('Maternity', 'Maternity')])
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.ward_type})"

class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ward.name} - Bed {self.bed_number}"

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"

class Patient(models.Model):
    # Demographics
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M','Male'), ('F','Female'), ('O','Other')], null=True)
    blood_group = models.CharField(max_length=5, blank=True)
    
    # Contact & Insurance
    contact_number = models.CharField(max_length=20, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True)
    allergies = models.TextField(blank=True, help_text="List any known allergies")

    # Hospital Data
    assigned_bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, null=True, blank=True)
    scan_file_3d = models.FileField(upload_to='models_3d/', blank=True, null=True)
    admission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VitalSign(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=20, help_text="e.g., 120/80")
    heart_rate = models.IntegerField(help_text="BPM")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, help_text="Fahrenheit or Celsius")
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'), 
        ('Completed', 'Completed'), 
        ('Cancelled', 'Cancelled')
    ], default='Scheduled')
    reason = models.CharField(max_length=255, blank=True)

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Insurance', 'Insurance')], blank=True)

    def total_amount(self):
        return sum(item.cost for item in self.items.all())
    
    def __str__(self):
        return f"Invoice #{self.id} - {self.patient}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
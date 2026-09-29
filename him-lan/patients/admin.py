from django.contrib import admin
from .models import Department, Ward, Bed, Doctor, Patient, VitalSign, Appointment, Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date_issued', 'total_amount', 'is_paid')
    list_filter = ('is_paid', 'payment_method')
    inlines = [InvoiceItemInline]

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'assigned_bed', 'admission_date')
    search_fields = ('first_name', 'last_name', 'contact_number')
    list_filter = ('gender', 'blood_group')

class BedAdmin(admin.ModelAdmin):
    list_display = ('bed_number', 'ward', 'is_occupied')
    list_filter = ('is_occupied', 'ward')

admin.site.register(Department)
admin.site.register(Ward)
admin.site.register(Bed, BedAdmin)
admin.site.register(Doctor)
admin.site.register(Patient, PatientAdmin)
admin.site.register(VitalSign)
admin.site.register(Appointment)
admin.site.register(Invoice, InvoiceAdmin)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Doctor, Appointment, Invoice, Bed


def dashboard(request):
    total_beds = Bed.objects.count()

    occupied_beds = (
        Bed.objects.filter(is_occupied=True).count()
        if hasattr(Bed, "is_occupied")
        else 0
    )

    bed_occupancy_rate = (
        occupied_beds / total_beds * 100
        if total_beds > 0
        else 0
    )

    available_beds = max(0, total_beds - occupied_beds)

    total_revenue = 0

    try:
        paid_invoices = Invoice.objects.filter(is_paid=True)

        total_revenue = sum(
            inv.total_amount()
            for inv in paid_invoices
            if hasattr(inv, "total_amount")
        )
    except Exception:
        total_revenue = 0

    context = {
        "total_patients": Patient.objects.count(),
        "active_doctors": Doctor.objects.count(),
        "pending_appointments": Appointment.objects.count(),
        "total_revenue": total_revenue,
        "bed_occupancy_rate": round(bed_occupancy_rate, 1),
        "available_beds": available_beds,
        "recent_patients": Patient.objects.all().order_by("-id")[:5],
    }

    return render(request, "patients/dashboard.html", context)


def patient_list(request):
    patients = Patient.objects.all().order_by("-id")

    return render(
        request,
        "patients/patient_list.html",
        {"patients": patients},
    )


def patient_add(request):
    from .forms import PatientForm

    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm()

    return render(
        request,
        "patients/patient_form.html",
        {"form": form},
    )


def patient_edit(request, pk):
    from .forms import PatientForm

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)

    return render(
        request,
        "patients/patient_form.html",
        {"form": form},
    )


def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")

    return render(
        request,
        "patients/patient_confirm_delete.html",
        {"object": patient},
    )


def webgl_viewer(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    return render(
        request,
        "patients/webgl_viewer.html",
        {"patient": patient},
    )


def discharge_pdf(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    return render(
        request,
        "patients/discharge_pdf.html",
        {"patient": patient},
    )

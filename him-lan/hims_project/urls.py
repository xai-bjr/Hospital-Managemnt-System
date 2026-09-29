from django.contrib import admin
from django.urls import path

from patients import views


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Patients
    path(
        "patients/",
        views.patient_list,
        name="patient_list",
    ),

    path(
        "patients/add/",
        views.patient_add,
        name="patient_add",
    ),

    path(
        "patients/<int:pk>/edit/",
        views.patient_edit,
        name="patient_edit",
    ),

    path(
        "patients/<int:pk>/delete/",
        views.patient_delete,
        name="patient_delete",
    ),

    # Patient 3D viewer
    path(
        "patients/<int:pk>/webgl/",
        views.webgl_viewer,
        name="webgl_viewer",
    ),

    # Discharge document
    path(
        "patients/<int:pk>/discharge/",
        views.discharge_pdf,
        name="discharge_pdf",
    ),
]

from flask import render_template
from flask_login import current_user


def list_patients(patients):
    return render_template(
        "patients.html",
        patients=patients,
        title="Lista de pacientes",
        current_user=current_user,
    )

def create_patient():
    return render_template(
        "create_patient.html", title="Crear Pacientes", current_user=current_user
    )

def update_patient(patient):
    return render_template(
        "update_patient.html",
        title="Editar paciente",
        patient=patient,
        current_user=current_user,
    )

from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.patient_model import Patient
from views import patient_view

from utils.decorators import role_required

patient_bp = Blueprint("patient", __name__)


@patient_bp.route("/patients")
@login_required
def list_patients():
    patients = patient.get_all()
    return patient_view.list_patients(patients)


@patient_bp.route("/patients/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_patient():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            last_name = request.form["last_name"]
            ci = request.form.get("ci")
            birth_date = request.form["birth_date"]
            patient = patient(name=name, last_name=last_name, ci=ci, birth_date=birth_date)
            patient.save()
            flash("Paciente creado exitosamente", "success")
            return redirect(url_for("patient.list_patients"))
        else:
            return jsonify({"message": "Unlast_nameized"}), 403
    return patient_view.create_patient()


@patient_bp.route("/patients/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_patient(id):
    patient = patient.get_by_id(id)
    if not patient:
        return "Paciente no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            last_name = request.form["last_name"]
            ci = request.form.get("ci")
            birth_date = request.form["birth_date"]
            patient.update(name=name, last_name=last_name, ci=ci, birth_date=birth_date)
            flash("Paciente actualizado exitosamente", "success")
            return redirect(url_for("patient.list_patients"))
        else:
            return jsonify({"message": "Unlast_nameized"}), 403
    return patient_view.update_patient(patient)


@patient_bp.route("/patients/<int:id>/delete")
@login_required
@role_required("admin")
def delete_patient(id):
    patient = patient.get_by_id(id)
    if not patient:
        return "Paciente no encontrado", 404
    if current_user.has_role("admin"):
        patient.delete()
        flash("Paciente eliminado exitosamente", "success")
        return redirect(url_for("patient.list_patients"))
    else:
        return jsonify({"message": "Unlast_nameized"}), 403

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Gpu, Cpu, Motherboard, Ram, Storage, Case, Psu, Build
from sqlalchemy.sql import func
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user = current_user)



@views.route('/create-build', methods=['GET', 'POST'])
@login_required
def create_build():
    if request.method == 'POST':
        gpu_id = request.form.get('gpu_id')
        cpu_id = request.form.get('cpu_id')
        motherboard_id = request.form.get('motherboard_id')
        ram_id = request.form.get('ram_id')
        psu_id = request.form.get('psu_id')
        storage_id = request.form.get('storage_id')
        case_id = request.form.get('case_id')

        # Create a new build and save it to the database
        new_build = Build(
            user_id=current_user.id,
            gpu_id=gpu_id,
            cpu_id=cpu_id,
            motherboard_id=motherboard_id,
            ram_id=ram_id,
            psu_id=psu_id,
            storage_id=storage_id,
            case_id=case_id,
            total_cost=0,  # Calculate total cost if needed
            build_date=func.now()
        )
        db.session.add(new_build)
        db.session.commit()
        flash("Build created successfully!", category='success')
        return redirect(url_for('views.home'))

    # Fetch data for dropdowns
    gpus = Gpu.query.all()
    cpus = Cpu.query.all()
    motherboards = Motherboard.query.all()
    rams = Ram.query.all()
    psus = Psu.query.all()
    storages = Storage.query.all()
    cases = Case.query.all()

    return render_template(
        "createbuild.html",
        gpus=gpus,
        cpus=cpus,
        motherboards=motherboards,
        rams=rams,
        psus=psus,
        storages=storages,
        cases=cases
    )



@views.route('/view-builds', methods=['GET'])
@login_required
def view_builds():
    # Fetch all builds for the current user
    builds = Build.query.filter_by(user_id=current_user.id).all()

    # Calculate the total cost for each build
    for build in builds:
        build.total_cost = (
            build.gpu.msrp +
            build.cpu.msrp +
            build.motherboard.msrp +
            build.ram.msrp +
            build.storage.msrp +
            build.psu.msrp +
            build.case.msrp
        )

    return render_template("viewbuild.html", builds=builds)


@views.route('/delete-build/<int:build_id>', methods=['GET', 'POST'])
@login_required
def delete_build(build_id):
    build = Build.query.get_or_404(build_id)

    # Ensure the build belongs to the current user
    if build.user_id != current_user.id:
        flash("You do not have permission to delete this build.", category='error')
        return redirect(url_for('views.view_builds'))

    if request.method == 'POST':
        db.session.delete(build)
        db.session.commit()
        flash("Build deleted successfully!", category='success')
        return redirect(url_for('views.view_builds'))

    return render_template("delete_build.html", build=build)


@views.route('/edit-build/<int:build_id>', methods=['GET', 'POST'])
@login_required
def edit_build(build_id):
    build = Build.query.get_or_404(build_id)

    # Ensure the build belongs to the current user
    if build.user_id != current_user.id:
        flash("You do not have permission to edit this build.", category='error')
        return redirect(url_for('views.view_builds'))

    if request.method == 'POST':
        build.gpu_id = request.form.get('gpu_id')
        build.cpu_id = request.form.get('cpu_id')
        build.motherboard_id = request.form.get('motherboard_id')
        build.ram_id = request.form.get('ram_id')
        build.psu_id = request.form.get('psu_id')
        build.storage_id = request.form.get('storage_id')
        build.case_id = request.form.get('case_id')

        # Recalculate total cost
        build.total_cost = (
            build.gpu.msrp +
            build.cpu.msrp +
            build.motherboard.msrp +
            build.ram.msrp +
            build.storage.msrp +
            build.psu.msrp +
            build.case.msrp
        )

        db.session.commit()
        flash("Build updated successfully!", category='success')
        return redirect(url_for('views.view_builds'))

    # Fetch data for dropdowns
    gpus = Gpu.query.all()
    cpus = Cpu.query.all()
    motherboards = Motherboard.query.all()
    rams = Ram.query.all()
    psus = Psu.query.all()
    storages = Storage.query.all()
    cases = Case.query.all()

    return render_template(
        "edit_build.html",
        build=build,
        gpus=gpus,
        cpus=cpus,
        motherboards=motherboards,
        rams=rams,
        psus=psus,
        storages=storages,
        cases=cases
    )


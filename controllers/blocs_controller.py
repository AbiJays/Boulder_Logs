from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.bloc import Bloc
import repositories.boulder_repository as boulder_repository
import repositories.bloc_repository as bloc_repository


blocs_blueprint = Blueprint("blocs", __name__)

# INDEX
@blocs_blueprint.route("/blocs")
def blocs():
    blocs = bloc_repository.select_all()
    return render_template("blocs/index.html", all_blocs = blocs)

# NEW
@blocs_blueprint.route("/blocs/new", methods=["GET"])
def new_bloc():
    boulders = boulder_repository.select_all()
    return render_template("blocs/new.html", all_boulders = boulders)

# CREATE
@blocs_blueprint.route("/blocs", methods=["POST"])
def create_bloc():
    name = request.form["name"]
    grade = request.form["grade"]
    wall_angle = request.form["wall_angle"]
    boulder_id = request.form["boulder_id"]
    completed = request.form["completed"]
    boulder = boulder_repository.select(boulder_id)
    bloc = Bloc(name, grade, wall_angle, boulder, completed)
    bloc_repository.save(bloc)
    return redirect("/blocs")

# SHOW
@blocs_blueprint.route("/blocs/<id>", methods= ["GET"])
def show_bloc(id):
    bloc = bloc_repository.select(id)
    return render_template("blocs/show.html", bloc = bloc)

# EDIT
@blocs_blueprint.route("/blocs/<id>/edit", methods=["GET"])
def edit_bloc(id):
    bloc = bloc_repository.select(id)
    return render_template("blocs/edit.html", bloc = bloc)


# DELETE(id)
@blocs_blueprint.route("/blocs/<id>/delete", methods=["POST"])
def delete_bloc(id):
    bloc_repository.delete(id)
    return redirect("/blocs")
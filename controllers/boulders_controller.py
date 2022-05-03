from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.boulder import Boulder
import repositories.boulder_repository as boulder_repository

boulders_blueprint = Blueprint("boulders", __name__)

# INDEX
@boulders_blueprint.route("/boulders")
def boulders():
    boulders = boulder_repository.select_all()
    return render_template("boulders/index.html", all_boulders = boulders)

# NEW
@boulders_blueprint.route("/boulders/new", methods = ["GET"])
def new_boulder():
    return render_template("boulders/new.html")

# CREATE
@boulders_blueprint.route("/boulders", methods=["POST"])
def create_boulder():
    name = request.form["name"]
    rock_type = request.form["rock_type"]
    boulder = Boulder(name, rock_type)
    boulder_repository.save(boulder)
    return redirect("/boulders")

# SHOW
@boulders_blueprint.route("/boulders/<id>", methods= ["GET"])
def show_boulder(id):
    boulder = boulder_repository.select(id)
    return render_template("boulders/show.html", boulder = boulder)

# EDIT
@boulders_blueprint.route("/boulders/<id>/edit", methods=["GET"])
def edit_boulder(id):
    boulder = boulder_repository.select(id)
    return render_template("boulders/edit.html", boulder = boulder)

# UPDATE
@boulders_blueprint.route("/boulders/<id>", methods=["POST"])
def update_boulder(id):
    name = request.form["name"]
    rock_type = request.form["rock_type"]
    boulder = Boulder(name, rock_type, id)
    boulder_repository.update(boulder)
    return redirect("/boulders")

# DELETE(id)
@boulders_blueprint.route("/boulders/<id>/delete", methods=["POST"])
def delete_boulder(id):
    boulder_repository.delete(id)
    return redirect("/boulders")
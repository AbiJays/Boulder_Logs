from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.bloc import Bloc
import repositories.bloc_repository as bloc_repository

blocs_blueprint = Blueprint("blocs", __name__)

@blocs_blueprint.route("/blocs")
def blocs():
    blocs = bloc_repository.select_all()
    return render_template("blocs/index.html", all_blocs = blocs)
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.boulder import Boulder
import repositories.boulder_repository as boulder_repository

boulders_blueprint = Blueprint("boulders", __name__)

@boulders_blueprint.route("/boulders")
def boulders():
    boulders = boulder_repository.select_all()
    return render_template("boulders/index.html", all_boulders = boulders)
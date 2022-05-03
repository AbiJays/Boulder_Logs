from db.run_sql import run_sql

from models.bloc import Bloc
from models.boulder import Boulder
import repositories.boulder_repository as boulder_repository



def save(bloc):
    sql = "INSERT INTO blocs (name, grade, wall_angle, boulder_id, completed) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [bloc.name, bloc.grade, bloc.wall_angle, bloc.boulder.id, bloc.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    bloc.id = id
    return bloc

def select_all():
    blocs = []

    sql = "SELECT * FROM blocs"
    results = run_sql(sql)

    for row in results:
        boulder = boulder_repository.select(row["boulder_id"])
        bloc = Bloc(row["name"], row["grade"], row["wall_angle"], boulder, row["completed"], row["id"])
        blocs.append(bloc)
    return blocs

def select(id):
    bloc = None
    sql = "SELECT * FROM blocs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        boulder = boulder_repository.select(result["boulder_id"])
        bloc = Bloc(result["name"], result["grade"], result["wall_angle"], boulder, result["completed"], result["id"])
    return bloc

def update(bloc):
    sql = "UPDATE blocs SET (name, grade, wall_angle, boulder_id, completed) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [bloc.name, bloc.grade, bloc.wall_angle, bloc.boulder.id, bloc.completed, bloc.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM blocs"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM blocs WHERE id = %s"
    values = [id]
    run_sql(sql, values)
from db.run_sql import run_sql

from models.boulder import Boulder


def save(boulder):
    sql = "INSERT INTO boulders (name, rock_type) VALUES (%s,%s) RETURNING *"
    values = [boulder.name, boulder.rock_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    boulder.id = id
    return boulder

def select_all():
    boulders = []

    sql = "SELECT * FROM boulders"
    results = run_sql(sql)

    for row in results:
        boulder = Boulder(row['name'], row['rock_type'], row['id'])
        boulders.append(boulder)
    return boulders

def select(id):
    boulder = None
    sql = "SELECT * FROM boulders WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        boulder = Boulder(result["name"], result["rock_type"], result["id"])
    return boulder

def delete_all():
    sql = "DELETE FROM boulders"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM boulders WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(boulder):
    sql = "UPDATE boulders SET (name, rock_type) = (%s, %s) WHERE id = %s"
    values = [boulder.name, boulder.rock_type, boulder.id]
    run_sql(sql, values)
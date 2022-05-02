DROP TABLE IF EXISTS blocs;
DROP TABLE IF EXISTS boulders;

CREATE TABLE boulders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    rock_type VARCHAR(255)
);

CREATE TABLE blocs (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    grade VARCHAR(255),
    wall_angle VARCHAR(255),
    boulder_id INT REFERENCES boulders(id),
    completed BOOLEAN
);
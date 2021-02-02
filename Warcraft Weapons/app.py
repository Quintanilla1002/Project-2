import sqlalchemy
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

#Database Setup
rds_connection_string = "postgres:postgres@localhost:5432/Warcraft Weapons"
engine = create_engine(f'postgresql://{rds_connection_string}')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#classes
onehand_weapons  = Base.classes.onehand_weapons
mh_weapons  = Base.classes.mh_weapons
oh_weapons  = Base.classes.oh_weapons
ranged_weapons  = Base.classes.ranged_weapons
twoh_weapons  = Base.classes.twoh_weapons
#Session Link
session = Session(engine)

# Flask Setup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/v1.0/onehand_weapons")
def onehand():
    onehand_weps = session.query(onehand_weapons.id, 
    onehand_weapons.name, 
    onehand_weapons.quality, 
    onehand_weapons.min_damage, 
    onehand_weapons.max_damage, 
    onehand_weapons.dps).all()
    session.close()

    # Convert list of tuples into normal list
    onehand_table = []
    for id, name, quality, min_damage, max_damage, dps in onehand_weps:
        onehand_dict = {}
        onehand_dict["id"] = id
        onehand_dict["name"] = name
        onehand_dict["quality"] = quality
        onehand_dict["min_damage"] = min_damage
        onehand_dict["max_damage"] = max_damage
        onehand_dict["dps"] = dps
        onehand_table.append(onehand_dict)

    return jsonify(onehand_table)

@app.route("/api/v1.0/mh_weapons")
def mainhand():
    mh_weps = session.query(mh_weapons.id, 
    mh_weapons.name, 
    mh_weapons.quality, 
    mh_weapons.min_damage, 
    mh_weapons.max_damage, 
    mh_weapons.dps).all()
    session.close()

    # Convert list of tuples into normal list
    mh_table = []
    for id, name, quality, min_damage, max_damage, dps in mh_weps:
        mh_dict = {}
        mh_dict["id"] = id
        mh_dict["name"] = name
        mh_dict["quality"] = quality
        mh_dict["min_damage"] = min_damage
        mh_dict["max_damage"] = max_damage
        mh_dict["dps"] = dps
        mh_table.append(mh_dict)

    return jsonify(mh_table)

@app.route("/api/v1.0/oh_weapons")
def offhand():
    oh_weps = session.query(oh_weapons.id, 
    oh_weapons.name, 
    oh_weapons.quality, 
    oh_weapons.min_damage, 
    oh_weapons.max_damage, 
    oh_weapons.dps).all()
    session.close()

    # Convert list of tuples into normal list
    oh_table = []
    for id, name, quality, min_damage, max_damage, dps in oh_weps:
        oh_dict = {}
        oh_dict["id"] = id
        oh_dict["name"] = name
        oh_dict["quality"] = quality
        oh_dict["min_damage"] = min_damage
        oh_dict["max_damage"] = max_damage
        oh_dict["dps"] = dps
        oh_table.append(oh_dict)

    return jsonify(oh_table)

@app.route("/api/v1.0/ranged_weapons")
def rangedhand():
    ranged_weps = session.query(ranged_weapons.id, 
    ranged_weapons.name, 
    ranged_weapons.quality, 
    ranged_weapons.min_damage, 
    ranged_weapons.max_damage, 
    ranged_weapons.dps).all()
    session.close()

    # Convert list of tuples into normal list
    ranged_table = []
    for id, name, quality, min_damage, max_damage, dps in ranged_weps:
        ranged_dict = {}
        ranged_dict["id"] = id
        ranged_dict["name"] = name
        ranged_dict["quality"] = quality
        ranged_dict["min_damage"] = min_damage
        ranged_dict["max_damage"] = max_damage
        ranged_dict["dps"] = dps
        ranged_table.append(ranged_dict)

    return jsonify(ranged_table)

@app.route("/api/v1.0/twoh_weapons")
def twohand():
    twoh_weps = session.query(twoh_weapons.id, 
    twoh_weapons.name, 
    twoh_weapons.quality, 
    twoh_weapons.min_damage, 
    twoh_weapons.max_damage, 
    twoh_weapons.dps).all()
    session.close()

    # Convert list of tuples into normal list
    twoh_table = []
    for id, name, quality, min_damage, max_damage, dps in twoh_weps:
        twoh_dict = {}
        twoh_dict["id"] = id
        twoh_dict["name"] = name
        twoh_dict["quality"] = quality
        twoh_dict["min_damage"] = min_damage
        twoh_dict["max_damage"] = max_damage
        twoh_dict["dps"] = dps
        twoh_table.append(twoh_dict)

    return jsonify(twoh_table)

if __name__ == "__main__":
      app.run(debug=True)
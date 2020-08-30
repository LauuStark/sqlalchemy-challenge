import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify
Base = declarative_base()

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Msmn = Base.classes.measurement

Stt = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    """Home Page."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    """Precipitation per date"""

    results = session.query(Msmn.prcp, Msmn.date).\
    group_by(Msmn.date).\
    order_by(Msmn.date).all()

    session.close()

    prec = []
    for prec, date in results:
        prec_dict = {}
        prec_dict["prcp"] = prec
        prec_dict["date"] = date
        prec.append(prec_dict)


    return jsonify(prec)

@app.route("/api/v1.0/stations")
def precipitation():
    session = Session(engine)

    """List of stations"""

    results2 = session.query(Stt.station).all()

    session.close()

    stations = list(results2)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    """Temperatures"""

    date2 = dt.datetime(2016, 8, 18)
    results3 = session.query(Msmn.tobs).\
        filter(Msmn.station == "USC00519281").\
        filter(Msmn.date > date2).\
        order_by(Msmn.date.desc()).all()

        temps = list(results3)

        return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)






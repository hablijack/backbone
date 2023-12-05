#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging
from library.Scheduler import Scheduler
from library.Database import Database
from library.Sql import Sql
from waitress import serve
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
sql = Sql()
database = Database()
scheduler = Scheduler(database)
from library.Sql import Sql

@app.route('/health')
def health():
    return {'status': 'UP'}

@app.route('/')
def home():
    return render_template(
        'home.html',
        title="Habel Smarthome",
        description="Habel Smarthome Template."
    )

@app.route('/api/house/stats/temp/current.json')
def current_temp():
    solar_production = database.read(sql.generate_solarpanel_last_entry_query())
    return {'temperature_outside': solar_production[0][0]}

@app.route('/api/house/power/current.json')
def current_power():
    solar_production = database.read(sql.generate_solarpanel_last_entry_query())
    print(solar_production)
    return {'house_consumption': 3600, 'solar_production': solar_production[0][1]}

def init_database():
    database.execute(sql.generate_solarpanel_table_stmt())
    database.execute(sql.generate_solarpanel_index_stmt())
    database.execute(sql.generate_zoe_table_stmt())
    database.execute(sql.generate_zoe_index_stmt())

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s [%(name)s] %(message)s",
        datefmt='%d.%m.%Y %H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )
    init_database()
    scheduler.start()
    serve(app, port=8080)

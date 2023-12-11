#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging
from library.Scheduler import Scheduler
from library.Database import Database
from jobs.Poweropti import Poweropti
from library.Sql import Sql
from waitress import serve
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
sql = Sql()
database = Database()
scheduler = Scheduler(database)

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

@app.route('/api/zoe/battery/current.json')
def current_zoe():
    battery_percent = database.read(sql.generate_zoe_last_entry_query())
    return {'battery_percent': battery_percent[0][0], 'total_mileage': battery_percent[0][1]}

@app.route('/api/house/stats/temp/current.json')
def current_temp():
    solar_production = database.read(sql.generate_solarpanel_last_entry_query())
    return {'temperature_outside': solar_production[0][0]}

@app.route('/api/house/power/current.json')
def current_power():
    solar_production = database.read(sql.generate_solarpanel_last_entry_query())
    house_consumption = database.read(sql.generate_poweropti_last_entry_query())
    return {'house_consumption': house_consumption[0][0], 'solar_production': solar_production[0][1]}

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

def init_database():
    database.execute(sql.generate_solarpanel_table_stmt())
    database.execute(sql.generate_solarpanel_index_stmt())
    database.execute(sql.generate_zoe_table_stmt())
    database.execute(sql.generate_zoe_index_stmt())
    database.execute(sql.generate_poweropti_table_stmt())
    database.execute(sql.generate_poweropti_index_stmt())

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

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging
from library.Scheduler import Scheduler
from library.Configuration import Configuration
from library.Database import Database
from waitress import serve
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
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
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )

def init_database():
    sql = Sql()
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

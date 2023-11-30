#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
import logging
from library.Scheduler import Scheduler
from library.Configuration import Configuration
from library.Database import Database
from waitress import serve
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
database = Database()
scheduler = Scheduler(database)
from library.Sql import Sql

@app.route('/health')
def health():
    return {'status': 'UP'}

def init_database():
    sql = Sql()
    database.execute(sql.generate_solarpanel_table_stmt())
    database.execute(sql.generate_solarpanel_index_stmt())

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

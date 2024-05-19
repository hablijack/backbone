#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
from jobs.Fritzbox import Fritzbox
from jobs.Poweropti import Poweropti
from jobs.Zoe import Zoe
from library.Database import Database
from library.Configuration import Configuration

class Scheduler():

    def __init__(self, database):
        self.config = Configuration()
        self.database = database
        self.scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Berlin'})
        self.register_jobs()

    def start(self):
        self.scheduler.start()

    def register_jobs(self):
        if self.config.scheduler_active():
            self.scheduler.add_job(Fritzbox.fetch, 'interval', [self.database], minutes=1)
            self.scheduler.add_job(Poweropti.fetch, 'interval', [self.database], minutes=1)
            self.scheduler.add_job(Zoe.fetch, 'interval', [self.database], minutes=15)
            self.scheduler.add_job(Database.cleanup, 'cron', [self.database], hour='10', minute='30')
        else: 
            pass

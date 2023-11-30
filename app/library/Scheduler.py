#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
from jobs.Fritzbox import Fritzbox
from jobs.Zoe import Zoe


class Scheduler():

    def __init__(self, database):
        self.database = database
        self.scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Berlin'})
        self.register_jobs()

    def start(self):
        self.scheduler.start()

    def register_jobs(self):
        self.scheduler.add_job(Fritzbox.fetch, 'interval', [self.database], minutes=1)
        self.scheduler.add_job(Zoe.fetch, 'interval', [self.database], minutes=10)

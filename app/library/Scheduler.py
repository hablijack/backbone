#!/usr/bin/python3
# -*- coding: utf-8 -*-

from apscheduler.schedulers.background import BackgroundScheduler
from jobs.Fritzbox import Fritzbox


class Scheduler():

    def __init__(self):
        Fritzbox.fetch()
        self.scheduler = BackgroundScheduler()
        self.register_jobs()

    def start(self):
        self.scheduler.start()

    def register_jobs(self):
        self.scheduler.add_job(Fritzbox.fetch, 'interval', minutes=5)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from library.sql import Sql
import logging


class ApiZoeBattery(RequestHandler):

    def initialize(self, database):
        self.logger = logging.getLogger('API_ZOE_BATTERY_HANDLER')
        self.database = database
        self.sql = Sql()

    def get(self):
        self.logger.info("... requesting zoe battery status via json api!")
        battery_percent = self.database.read(self.sql.generate_zoe_last_entry_query())
        self.write({'battery_percent': battery_percent[0][0], 'total_mileage': battery_percent[0][1]})

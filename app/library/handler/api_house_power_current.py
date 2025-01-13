#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from library.sql import Sql
import logging


class ApiHousePowerCurrent(RequestHandler):

    def initialize(self, database):
        self.logger = logging.getLogger('API_HOUSE_POWER_CURRENT')
        self.database = database
        self.sql = Sql()

    def get(self):
        solar_production = self.database.read(self.sql.generate_solarpanel_last_entry_query())
        house_consumption = self.database.read(self.sql.generate_poweropti_last_entry_query())
        self.write({'house_consumption': house_consumption[0][0], 'solar_production': solar_production[0][1]})

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from library.sql import Sql
import logging


class ApiHouseTempCurrent(RequestHandler):

    def initialize(self, database):
        self.logger = logging.getLogger('API_HOUSE_TEMP_CURRENT')
        self.database = database
        self.sql = Sql()

    def get(self):
        solar_production = self.database.read(self.sql.generate_solarpanel_last_entry_query())
        self.write({'temperature_outside': solar_production[0][0]})

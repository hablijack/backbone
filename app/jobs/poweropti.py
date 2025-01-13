#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from library.sql import Sql
from http.client import HTTPSConnection
from base64 import b64encode
from library.Configuration import Configuration
import json


class Poweropti():

    @staticmethod
    def fetch(database):
        sql = Sql()
        config = Configuration()
        logger = logging.getLogger("Poweropti")
        try:
            c = HTTPSConnection("backend.powerfox.energy")
            token = b64encode(f"{config.poweropti_user()}:{config.poweropti_password()}".encode('utf-8')).decode("ascii")
            headers = { 'Authorization' : f'Basic {token}' }
            c.request('GET', '/api/2/my/1097bd718c80/current?unit=wh', headers=headers)
            res = c.getresponse()
            data = res.read().decode("utf-8")
            insert_stmt = sql.generate_poweropti_insert_stmt(json.loads(data)['watt'])
            database.execute(insert_stmt)
        except Exception as e:
            logger.error("Error: %s. Cannot get Poweropti data." % e)

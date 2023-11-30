#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzhomeauto import FritzHomeAutomation
from library.Configuration import Configuration
from library.Sql import Sql

class Fritzbox():

    @staticmethod
    def fetch(database):
        config = Configuration()
        insert = ""
        sql = Sql()
        logger = logging.getLogger("Fritzbox")
        try:
            fc = FritzConnection(address=config.fritz_api_ip(), user=config.fritz_api_user(), password=config.fritz_api_pass())
            fh = FritzHomeAutomation(fc)
            garage_solar_socket = fh.get_device_information_by_identifier(config.fritz_garage_solar_ain())
            temp = garage_solar_socket['NewTemperatureCelsius'] * 0.1
            status = 1 if garage_solar_socket['NewPresent'] == 'CONNECTED' else 0
            power = garage_solar_socket['NewMultimeterPower'] / 100
            insert = sql.generate_solarpanel_insert_stmt(temp, status, power)
            database.execute(insert)
            balcony_solar_socket = fh.get_device_information_by_identifier(config.fritz_balcony_solar_ain())
            temp = balcony_solar_socket['NewTemperatureCelsius'] * 0.1
            status = 1 if balcony_solar_socket['NewPresent'] == 'CONNECTED' else 0
            power = balcony_solar_socket['NewMultimeterPower'] / 100 
            insert = sql.generate_solarpanel_insert_stmt(temp, status, power)        
            database.execute(insert)
        except Exception as e:
            logger.error("Error: %s. Cannot get Fritzbox data." % e)

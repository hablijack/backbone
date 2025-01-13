#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzhomeauto import FritzHomeAutomation
from library.Configuration import Configuration
from library.sql import Sql


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
            balcony_solar_socket = fh.get_device_information_by_identifier(config.fritz_balcony_solar_ain())

            balcony_temp = balcony_solar_socket['NewTemperatureCelsius'] * 0.1
            overall_status = 0
            if garage_solar_socket['NewPresent'] == 'CONNECTED' and balcony_solar_socket['NewPresent'] == 'CONNECTED':
                overall_status = 1
            balcony_power = balcony_solar_socket['NewMultimeterPower'] / 100 
            garage_power = garage_solar_socket['NewMultimeterPower'] / 100 
            insert = sql.generate_solarpanel_insert_stmt(balcony_temp, overall_status, balcony_power + garage_power)     
            database.execute(insert)
        except Exception as e:
            logger.error("Error: %s. Cannot get Fritzbox data." % e)

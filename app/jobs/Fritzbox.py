#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzhomeauto import FritzHomeAutomation
from library.Configuration import Configuration

class Fritzbox():

    @staticmethod
    def fetch():
        stats = { }
        config = Configuration()
        logger = logging.getLogger("Fritzbox")
        try:
            fc = FritzConnection(address=config.fritz_api_ip(), user=config.fritz_api_user(), password=config.fritz_api_pass())
            fh = FritzHomeAutomation(fc)
            garage_solar_socket = fh.get_device_information_by_identifier(config.fritz_garage_solar_ain())
            stats['id'] = 'GARAGE_SOLAR'
            stats['power'] = garage_solar_socket['NewMultimeterPower'] / 100
            stats['status'] = garage_solar_socket['NewPresent']
            stats['temperature'] = garage_solar_socket['NewTemperatureCelsius'] / 10
        except Exception as e:
            logger.error("Error: %s. Cannot get Fritzbox." % e)
        print(stats)

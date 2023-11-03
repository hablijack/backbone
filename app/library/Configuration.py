#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

""""
Read configuration from environment variables
"""


class Configuration:

    def fritz_api_ip(self):
        return os.getenv('FRITZ_API_IP')

    def fritz_api_pass(self):
        return os.getenv('FRITZ_API_PASS') 

    def fritz_api_user(self):
        return os.getenv('FRITZ_API_USER')

    def fritz_garage_solar_ain(self):
        return os.getenv('FRITZ_GARAGE_SOLAR_AIN')
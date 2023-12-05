#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

""""
Read configuration from environment variables
"""


class Configuration:

    def scheduler_active(self):
        return os.getenv('SCHEDULER_ACTIVE')

    def postgres_password(self):
        return os.getenv('POSTGRES_PASSWORD')

    def postgres_user(self):
        return os.getenv('POSTGRES_USER')

    def postgres_db(self):
        return os.getenv('POSTGRES_DB')

    def postgres_host(self):
        return os.getenv('POSTGRES_HOST')

    def fritz_api_ip(self):
        return os.getenv('FRITZ_API_IP')

    def fritz_api_pass(self):
        return os.getenv('FRITZ_API_PASS') 

    def fritz_api_user(self):
        return os.getenv('FRITZ_API_USER')

    def fritz_garage_solar_ain(self):
        return os.getenv('FRITZ_GARAGE_SOLAR_AIN')
    
    def fritz_balcony_solar_ain(self):
        return os.getenv('FRITZ_BALCONY_SOLAR_AIN')

    def zoe_username(self):
        return os.getenv('ZOE_USERNAME')

    def zoe_password(self):
        return os.getenv('ZOE_PASSWORD')
    
    def zoe_account_id(self):
        return os.getenv('ZOE_ACCOUNT_ID')

    def zoe_vehicle_id(self):
        return os.getenv('ZOE_VEHICLE_ID')
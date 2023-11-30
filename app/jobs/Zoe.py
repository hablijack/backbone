#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import aiohttp
import asyncio
from library.Configuration import Configuration
from library.Configuration import Configuration
from renault_api.renault_client import RenaultClient
from library.Sql import Sql

class Zoe():

    @staticmethod
    async def renault_request(database):
        insert = ""
        sql = Sql()
        try:
            logger = logging.getLogger("Zoe")
            config = Configuration()
            async with aiohttp.ClientSession() as websession:
                client = RenaultClient(websession=websession, locale="de_DE")
                await client.session.login(config.zoe_username(), config.zoe_password())
                account = await client.get_api_account(config.zoe_account_id())
                vehicle = await account.get_api_vehicle(config.zoe_vehicle_id())
                cockpit_data = await vehicle.get_cockpit()
                battery_data = await vehicle.get_battery_status()
                insert = sql.generate_zoe_insert_stmt(battery_data.batteryLevel, cockpit_data.totalMileage)
                database.execute(insert)            
        except Exception as e:
            logger.error("Error: %s. Cannot get Zoe data." % e)

    @staticmethod
    def fetch(database):
        asyncio.run(Zoe.renault_request(database))

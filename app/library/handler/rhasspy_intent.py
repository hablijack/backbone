#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from tornado.escape import json_decode
import logging
from datetime import datetime


class RhasspyIntent(RequestHandler):

    def initialize(self, database):
        self.logger = logging.getLogger('RHASSPY_INTENT')
        self.database = database

    def post(self):
        json_body = json_decode(self.request.body)
        if json_body['intent']['name'] == "GetTime":
            now = datetime.now()
            sentence = "Es ist jetzt " + str(now.hour) + " Uhr"
            if now.minute > 0:  
                sentence += " und " + str(now.minute) + " Minuten"
            self.write({'speech': {'text': sentence}})

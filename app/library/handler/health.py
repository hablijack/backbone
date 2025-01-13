#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
import logging


class Health(RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger('HEALTH_HANDLER')

    def get(self):
        self.logger.info("... rendering HealthPage!")
        self.write({'status': 'UP'})

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
import logging


class Homepage(RequestHandler):

    def initialize(self):
        self.logger = logging.getLogger('HOMEPAGE_HANDLER')

    def get(self):
        self.logger.info("... rendering Homepage!")
        self.render('index.html')
#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# Copyright (c) 2015 Maik Lindner

from variety.Util import Util
from variety.plugins.IQuoteSource import IQuoteSource
from locale import gettext as _
 
import logging
import random
 
logger = logging.getLogger("variety")
 
class ZitateSource(IQuoteSource):
    @classmethod
    def get_info(cls):
        return {
            "name": "Zitate, deutsch",
            "description": _("Zitate vom zitate.eu RSS feed."),
            "author": "Maik Lindner",
            "version": "0.1"
        }

    def supports_search(self):
        return False
        
    def get_quote(self):
        url = "http://www.zitate.eu/beruehmte-personen/zitate/rss/zz0/feed.xml"
 
        zitat = Util.xml_soup(url)
        zitat = zitat.find("title").contents[0].strip()
        return [{"quote": zitat, "author": "", "sourceName": "zitate.eu", "link": ""}]

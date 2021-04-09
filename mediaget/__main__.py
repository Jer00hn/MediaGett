
#from __future__ import print_function, unicode_literals

#import datetime
#import getopt
#import io
#import locale
import logging
import os
#import random
#import re
#import shutil
#import signal
#import socket
#import subprocess
import sys
#import threading
#import time
#from builtins import object
#from builtins import str

import json

#from medusa import (
#    cache, db, exception_handler, helpers,
#    logger as app_logger, metadata, name_cache, naming,
#    network_timezones, process_tv, providers, subtitles
#)
from mediaget.app import app
#from medusa.common import SD, SKIPPED, WANTED
#from medusa.config import (
#    CheckSection, ConfigMigrator, check_setting_bool,
#    check_setting_float, check_setting_int,
#    check_setting_list, check_setting_str,
#    load_provider_setting, save_provider_setting
#)
#from medusa.databases import cache_db, failed_db, main_db
#from medusa.failed_history import trim_history
#from medusa.indexers.config import INDEXER_TVDBV2, INDEXER_TVMAZE
#from medusa.init.filesystem import is_valid_encoding
#from medusa.providers.generic_provider import GenericProvider
#from medusa.providers.nzb.newznab import NewznabProvider
#from medusa.providers.torrent.rss.rsstorrent import TorrentRssProvider
#from medusa.providers.torrent.torznab.torznab import TorznabProvider
#from medusa.queues import show_queue
#from medusa.queues.event_queue import Events
#from medusa.schedulers import (
#    download_handler, episode_updater, scheduler, #show_updater, trakt_checker
#)
#from medusa.search.backlog import BacklogSearchScheduler, BacklogSearcher
#from medusa.search.daily import DailySearcher
#from medusa.search.proper import ProperFinder
#from medusa.search.queue import ForcedSearchQueue, PostProcessQueue, SearchQueue, SnatchQueue
#from medusa.server.core import AppWebServer
#from medusa.system.shutdown import Shutdown
#from medusa.themes import read_themes
#from medusa.tv import Series
#from medusa.updater.version_checker import CheckVersion

#import trakt


logger = logging.getLogger(__name__)


class Application(object):
    """Main application module."""

    def __init__(self):
        
        """Init method."""
        # system event callback for shutdown/restart
#        app.events = Events(self.shutdown)
        self.console_logging = True
           

    def start(self, args):
        """Start Application."""
        app.instance = self
#        signal.signal(signal.SIGINT, self.sig_handler)
#        signal.signal(signal.SIGTERM, self.sig_handler)

        # do some preliminary stuff
        app.MY_ARGS = args
        app.SYS_ENCODING = sys.getfilesystemencoding()
        sys.stdout.write('Current Config dir: %s\n' % app.CONFIG_DIR)
   
        self.console_logging = (not hasattr(sys, 'frozen')) or (app.MY_NAME.lower().find('-console') > 0)

        
        # If they don't specify a config file then put it in the config dir
        if not app.CONFIG_FILE:
            app.CONFIG_FILE = os.path.join(app.CONFIG_DIR, 'config.json')
            
         # Load the config and publish it to the application package
        if self.console_logging and not os.path.isfile(app.CONFIG_FILE):
            sys.stdout.write('Unable to find %s, all settings will be default!\n' % app.CONFIG_FILE)
            
            # Make sure we can write to the config file
        if not os.access(app.CONFIG_FILE, os.W_OK):
            if os.path.isfile(app.CONFIG_FILE):
                raise SystemExit('Config file must be writeable: %s' % app.CONFIG_FILE)
            elif not os.access(os.path.dirname(app.CONFIG_FILE), os.W_OK):
                raise SystemExit('Config file root dir must be writeable: %s' % os.path.dirname(app.CONFIG_FILE))

        if os.path.isfile(app.CONFIG_FILE):
        	with open(app.CONFIG_FILE, encoding='utf-8') as fh:
        		app.CFG = json.load(fh)
        		self.loadconfig(console_logging=self.console_logging)
        
def main():
    # start application
    application = Application()
    application.start(sys.argv[1:])


if __name__ == '__main__':
    main()
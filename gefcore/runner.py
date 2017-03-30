from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gefcore.loggers import get_logger_by_env
from gefcore.script import main

import logging

def change_status_ticket(): pass

def send_result(result): pass

def run(params):
    try:
        logging.debug('Creating logger')
        logger = get_logger_by_env()
        change_status_ticket() # running
        result = main.run(params, logger)
        send_result(result)
        change_status_ticket() # success
    except Exception as error:
        change_status_ticket() #failed
        raise error

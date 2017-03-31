"""GEF CORE RUNNER"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
from gefcore.loggers import get_logger_by_env
from gefcore.script import main


def change_status_ticket():
    """Ticket status changer"""
    pass


def send_result(result):
    """Results sender"""
    pass


def run(params):
    """Runs the user script"""
    try:
        logging.debug('Creating logger')
        # Getting logger
        logger = get_logger_by_env()
        change_status_ticket()  # running
        result = main.run(params, logger)
        send_result(result)
        change_status_ticket()  # success
    except Exception as error:
        change_status_ticket()  # failed
        raise error

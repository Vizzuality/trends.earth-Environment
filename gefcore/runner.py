"""GEF CORE RUNNER"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ee
import os
import logging
from oauth2client.service_account import ServiceAccountCredentials

from gefcore.loggers import get_logger_by_env
from gefcore.script import main
from gefcore.api import patch_execution

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = os.getenv('ENV')
EE_SERVICE_ACOUNT = os.getenv('EE_SERVICE_ACCOUNT', None)
if EE_SERVICE_ACOUNT:
    logging.info('Authenticating earth engine')
    gee_credentials = ServiceAccountCredentials.from_p12_keyfile(
        os.getenv('EE_SERVICE_ACCOUNT', ''),
        os.path.join(PROJECT_DIR, 'privatekey.pem'),
        scopes = ee.oauth.SCOPE
    )

    ee.Initialize(gee_credentials)

def change_status_ticket():
    """Ticket status changer"""
    if ENV != 'dev':
        patch_execution(json={"status": "RUNNING"})
    else:
        logging.info('Channing to RUNNING')

def send_result(results):
    """Results sender"""
    if ENV != 'dev':
        patch_execution(json={"results": results, "status": "FINISHED"})
    else:
        logging.info('Finished -> Results:')
        logging.info(results)


def run(params):
    """Runs the user script"""
    try:
        logging.debug('Creating logger')
        # Getting logger
        logger = get_logger_by_env()
        change_status_ticket()  # running
        result = main.run(params, logger)
        send_result(result)
    except Exception as error:
        change_status_ticket()  # failed
        raise error

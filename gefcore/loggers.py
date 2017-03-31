"""GEF CORE LOGGER"""

import logging
import os


class LocalLogger(object):
    """Logger implementation for local (dev environment)"""

    @staticmethod
    def debug(text):
        """Debug Level"""
        logging.debug(text)

    @staticmethod
    def info(text):
        """Info Level"""
        logging.info(text)

    @staticmethod
    def warn(text):
        """Warn Level"""
        logging.warn(text)

    @staticmethod
    def error(text):
        """Error Level"""
        logging.error(text)

    @staticmethod
    def send_progress(progress):
        """Send Progress"""
        LocalLogger.info('Progress ' + progress + '%')


class ServerLogger(object):
    """Logger implementation for server (prod environment)"""

    @staticmethod
    def debug(text):
        """Debug Level"""
        pass

    @staticmethod
    def info(text):
        """Info Level"""
        pass

    @staticmethod
    def warn(text):
        """Warn Level"""
        pass

    @staticmethod
    def error(text):
        """Error Level"""
        pass

    @staticmethod
    def send_progress(progress):
        """Send Progress"""
        pass


LOGGERS = {
    "dev": LocalLogger,
    "prod": ServerLogger
}


def get_logger_by_env():
    """Get logger according to theenvironment"""
    env = os.getenv('ENV')
    logger = LOGGERS.get(env)
    return logger

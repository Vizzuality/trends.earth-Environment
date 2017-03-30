import logging
import os

class LocalLogger(object):
    def debug(self, text): 
        logging.debug(text)

    def info(self, text):
        logging.info(text)

    def warn(self, text):
        logging.warn(text)

    def error(self, text):
        logging.error(text)
        
    def send_progress(self, progress):
        self.info('Progress ' + progress + '%')


class ServerLogger(object):
    def debug(self, text): pass
    def info(self, text): pass
    def warn(self, text): pass
    def error(self, text): pass
    def sendprogress(self, progress): pass

LOGGERS = {
    "dev": LocalLogger,
    "prod": ServerLogger
}

def get_logger_by_env():
    env = os.getenv('ENV')
    logger = LOGGERS.get(env)
    return logger()

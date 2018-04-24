import logging


LOGGING_LEVEL = logging.INFO
logging.basicConfig(format="%(levelname)-7s %(name)-23s%(lineno)s:%(message)s", level=LOGGING_LEVEL)

DUMP_PATH = "./dumps/"
DUMP_EXTRACTION_REGEX_PATH = "./regex_dump_extraction.txt"

class Loggable():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

import logging

logging.basicConfig(format="%(levelname)-7s %(name)-15s%(lineno)s:%(message)s", level=logging.DEBUG)
DUMP_PATH = "./dumps/"
DUMP_EXTRACTION_REGEX_PATH = "./regex_dump_extraction.txt"

class Loggable():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

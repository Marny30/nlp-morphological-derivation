import logging

logging.basicConfig(format="%(levelname)7s %(name)13s: %(message)s")
DUMP_PATH = "./dumps/"
DUMP_EXTRACTION_REGEX_PATH = "./regex_dump_extraction.txt"

class Loggable():
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

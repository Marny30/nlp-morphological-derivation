#!/usr/bin/python3

import config
import re

class DumpExtractor(config.Loggable):
    def extract_info_from_file(self, dumpname):
        self.logger.debug("Lecture du dump '"+ dumpname + "'")
        path = config.DUMP_PATH + dumpname
        with open(path) as dumpfile:
            dumptext = dumpfile.read()
        self.logger.debug("Extraction de données")
        return self.extract_info_from_text(dumptext)

    def extract_info_from_text(self, dumptext):
        # ref : https://regex101.com/
        assert len(dumptext) > 0
        matcher = re.match(self.extractionregex, dumptext)
        res = matcher.groupdict()
        self.logger.debug("données extraites")
        return res
    
    def __init__(self):
        super().__init__()
        with open(config.DUMP_EXTRACTION_REGEX_PATH, 'r') as myfile:
            self.extractionregex = myfile.read()
        if self.extractionregex[-1] == '\n':
            self.extractionregex = self.extractionregex[:-1]

def main():
    import logging
    import pprint
    extractor = DumpExtractor()
    extractor.logger.setLevel(logging.DEBUG)
    info = extractor.extract_info_from_file("marin")
    # extractor.logger.info(info)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(info)

if __name__ == '__main__':
    main()

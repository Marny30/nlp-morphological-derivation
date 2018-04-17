#!/usr/bin/python3

import re
import config

class Relation(config.Loggable):
    def __init__(self, string):
        tokens = string.split(";")
        self.id = int(tokens[1])
        self.node1 = int(tokens[2])
        self.node2 = int(tokens[3])
        self.type = int(tokens[4])
    def __str__(self):
        return str(self.__dict__)

class Noeud(config.Loggable):
    def __init__(self, string):
        tokens = string.split(";")
        self.id = int(tokens[1])
        self.label = tokens[2][1:-1]  # on enlève les '' au début à et
                                      # à la fin
        self.type = int(tokens[3])
        
    def __str__(self):
        return str(self.__dict__)

class DumpParser(config.Loggable):
    # ref : https://regex101.com/
    META_INFO_REGEX = "\n*// DUMP pour le terme '[a-zA-Z]+' \(eid=(?P<id>\d+)\)\n*(?P<desc>[\W\w]*)\n\n\n\n"
    # NODE_REGEX = "// les noeuds/termes \(Entries\) : e;eid;'name';type;w;'formated name' \n\n(?P<nodes>[\d\D]*)\n\n// les types de relations"
    # REL_IN_REGEX = "// les relations ent.*\n(?P<rel_in>[\w\W]*)\n\n// END"
    # REL_OUT_REGEX = "// les relations sort.*\n\n(?P<rel_out>[\w\W]*)\n\n// les relations"
    
    def __init__(self, dumpname):
        super().__init__()
        self._parse_info_from_file(dumpname)

    def _parse_info_from_file(self, dumpname):
        self.logger.debug("Lecture du dump '"+ dumpname + "'")
        path = config.DUMP_PATH + dumpname
        with open(path) as dumpfile:
            dumptext = dumpfile.read()
        self._parse_info_from_text(dumptext)
        
    def _parse_info_from_text(self, dumptext):
        assert len(dumptext) > 0
        def parse_relations(text):
            res = []
            for line in text.split('\n'):
                res+=[Relation(line)]
            return res
        self.logger.debug("Extraction de données")
        matcher = re.match(DumpParser.META_INFO_REGEX, dumptext)
        self.desc = matcher.group('desc')
        self.id = (matcher.group('id'))

        splitted_dumptext = dumptext.split('\n')

        self.logger.debug("parsing metadata")
        for i, line in enumerate(splitted_dumptext):
            if line == "// les noeuds/termes (Entries) : e;eid;'name';type;w;'formated name' ":
                break
        splitted_dumptext = splitted_dumptext[i+2:]
        
        self.logger.debug("parsing nodes")
        self.nodes = []
        for i, line in enumerate(splitted_dumptext):
            if line == "":
                break
            else:
                self.nodes += [Noeud(line)]
        splitted_dumptext = splitted_dumptext[i+3:]

        self.rel_dict = {}
        self.logger.debug("parsing relations dict")
        for i, line in enumerate(splitted_dumptext):
            if line == "":
                break
            else:
                tokens = line.split(";")
                name = tokens[2][1:-1]
                self.rel_dict[name] = int(tokens[1])
                self.rel_dict[int(tokens[1])] = name
        splitted_dumptext = splitted_dumptext[i+3:]

        self.rel_out = []
        self.logger.debug("parsing outgoing relations")
        for i, line in enumerate(splitted_dumptext):
            if line == "":
                break
            else:
                self.rel_out += [Relation(line)]
        splitted_dumptext = splitted_dumptext[i+3:]

        self.rel_in = []
        self.logger.debug("parsing incoming relations")
        for i, line in enumerate(splitted_dumptext):
            if line == "":
                break
            else:
                self.rel_in += [Relation(line)]
        self.logger.debug("parsing finished")
        
    def __str__(self):
        res = "NODES\n"
        for x in self.nodes:
            res += "\t" + str(x) + "\n"
        res += "REL_OUT\n"
        for x in self.rel_in:
            res += "\t" + str(x) + "\n"
        res += "REL_IN\n"
        for x in self.rel_out:
            res += "\t" + str(x) + "\n"
        return res

def main():
    import logging
    word = "fioriture"
    dparser = DumpParser(word)
    dparser.logger.setLevel(logging.DEBUG)
    print(dparser)
    
if __name__ == '__main__':
    main()

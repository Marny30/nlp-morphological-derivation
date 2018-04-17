#!/usr/bin/python3


# class dump_

import dump_manager
import dump_analyzer_adaptater

class Dump_analyzer_factory:
    """ Factory design pattern """
    DM = dump_manager.DumpManager()
    def __init__(self):
        pass
    def create(self, mot):
        dump = self._getDump(mot)
        res = None
        if dump!='':
            res = dump_analyzer_adaptater.DumpAnalyzerAdaptater(mot)
        return res
    def _getDump(self, mot):
        return Dump_analyzer_factory.DM.get_dump(mot)
    def _hasDump(self, mot):
        return Dump_analyzer_factory.DM.has_dump(mot)

def main():
    import sys
    if len(sys.argv)==1:
        word = "manger"
    else:
        word = sys.argv[1]
        
    myfactory = Dump_analyzer_factory()
    analyzer = myfactory.create(word)

    print("Pos de '" + word + "' ?")
    tmp = analyzer.get_nodes_by_typename("n_pos")
    for x in tmp:
        print("\t", x)

    print("node n_data?")
    tmp = analyzer.get_nodes_by_typename("n_data")
    for x in tmp:
        print("\t", x)

if __name__ == '__main__':
    main()

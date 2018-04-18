#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dump_analyzer
class DumpAnalyzerAdaptater(dump_analyzer.DumpAnalyzer):
    """ Permet d'avoir une interface plus simple, de plus haut niveau pour
    la classe DumpAnalyzer 

    """
    rels_a_test = [
                   "r_associated",
                   "r_isA",
                   "r_family",
                   "r_lemma",
                   "r_agentif_role",
                   "r_lieu-1", "r_agent-1",
    ]
    rels_production = [
        "r_adj-verbe", "r_verbe-adj",
        "r_action_lieu", "r_lieu_action",
        "r_nomprop-adj", "r_nomprop-adv", 
        "r_verbe-action", "r_action-verbe",
        "r_adj-adv", "r_adv-adj"
    ]
    
    def get_all_associated_words(self):
        rels_to_test = DumpAnalyzerAdaptater.rels_a_test + DumpAnalyzerAdaptater.rels_production
        res = set()
        for relname in rels_to_test:
            if not relname in self.rel_dict.keys():
                continue
            rels = self.get_rels_by_typename(relname, incoming=True)
            for rel in rels:
                res.add(self.get_node_by_id(rel.node1).label)
            rels = self.get_rels_by_typename(relname, incoming=False)
            for rel in rels:
                res.add(self.get_node_by_id(rel.node2).label)
        return list(res)
    
    def get_associated_produced_word(self):  # todo
        res = set()
        # filtrage des bonnes relations
        rels_to_test = set()
        pos = self.get_pos()

        for relname in DumpAnalyzerAdaptater.rels_production:
            if not relname in self.rel_dict.keys():
                continue
            rels = self.get_rels_by_typename(relname, incoming=True)
            
            for rel in rels:
                res.add(self.get_node_by_id(rel.node1).label)
            rels = self.get_rels_by_typename(relname, incoming=False)
            
            for rel in rels:
                res.add(self.get_node_by_id(rel.node2).label)
        return list(res)
    
    def __init__(self, dumpname):
        super().__init__(dumpname)
        self.pos = self.get_pos()
            

    def _get_labels(self, mylist):
        res = []
        for elem in mylist:
            res += [elem.label]
        return res
    
    def get_pos(self):
        posnodes =  self.get_nodes_by_typename("n_pos")
        return self._get_labels(posnodes)

    def get_lemmas(self):
        lemmarels = self.get_rels_by_typename("r_lemma", incoming=False)
        res = []
        for rel in lemmarels:
            res += [self.get_node_by_id(rel.node2).label]
        return res

    def get_verb_group(self):
        datanodes = self.get_nodes_by_typename("n_data")
        res = None
        for node in datanodes:
            if node.label.startswith("Ver:Groupe"):
                res = node.label
        return res
    
    # def get_nodes_of_interest(self):
    #     for relname in DumpAnalyzerAdaptater.rels_a_test:
    #         if not relname in self.rel_dict.keys():
    #             continue
    #         print("  " + relname)
    #         tmp = self.get_rels_by_typename(relname, incoming=True)
    #         for x in tmp:
    #             print("    in:\t", self._rel_to_string(x))
    #         tmp = self.get_rels_by_typename(relname, incoming=False)
    #         for x in tmp:
    #             print("    out:", self._rel_to_string(x))

def main():
    import sys
    import dump_analyzer_factory
    if len(sys.argv)==1:
        word = "changer"
    else:
        word = sys.argv[1]
        
    myfactory = dump_analyzer_factory.Dump_analyzer_factory()
    analyzer = myfactory.create(word)

    if not analyzer:
        return
    
    print("pos de " + word + "?")
    print(analyzer.get_pos())

    print("lemma de " + word + "?")
    print(analyzer.get_lemmas())

    print("groupe verbale de " + word + "?")
    print(analyzer.get_verb_group())

    # print("mot produit associé à " + word + "?")
    # print(analyzer.get_associated_produced_word())

    print("mot liés à " + word + "?")
    print(analyzer.get_all_associated_words())

if __name__ == '__main__':
    main()

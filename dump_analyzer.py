#!/usr/bin/python3

# import config
import re
import dump_parser


class DumpAnalyzer(dump_parser.DumpParser):
    NODE_DICT = {
        'n_term':1,
        'n_form':2,
        'n_pos':4,
        'n_flpot':6,
        'n_data':18,
        'n_data_pot':36,
        'n_link':444,
        'n_wikipedia':777
    }
    def __init__(self, dumpname):
        super().__init__(dumpname)
        
    def get_nodes_by_type(self, ntype):
        res = []
        for rel in self.nodes:
            if rel.type == ntype:
                res.append(rel)
        return res

    def get_node_by_id(self, nid):
        res = None
        for node in self.nodes:
            if node.id == nid:
                res = node
        return res

    def get_nodes_by_typename(self, name):
        return self.get_nodes_by_type(DumpAnalyzer.NODE_DICT[name])

    def get_rel_by_id(self, rid, incoming=True):
        res = None
        if incoming:
            target = self.rel_in
        else:
            target = self.rel_out
        for rel in self.rel_in:
            if rel.id == rid:
                res = rel
        return res
    
    def get_rels_by_type(self, ntype, incoming=True):
        if incoming:
            target = self.rel_in
        else:
            target = self.rel_out
        res = []
        for rel in target:
            if rel.type == ntype:
                res.append(rel)
        return res

    def get_rels_by_typename(self, relname,  incoming=True):
        if relname not in self.rel_dict.keys():
            return []
        return self.get_rels_by_type(self.rel_dict[relname], incoming)

    def _rel_to_string(self, rel):
        incominglabel = self.get_node_by_id(rel.node1).label
        outgoinglabel = self.get_node_by_id(rel.node2).label
        rel_name = self.rel_dict[rel.type]
        # print(incominglabel, " --", rel_name, "-> ", outgoinglabel)
        res = incominglabel + " --[" + rel_name + "]-> " + outgoinglabel
        return res
        
    def __str__(self):
        res = "NODES\n"
        for x in self.nodes:
            res += "\t" + str(x) + "\n"
        res += "REL_OUT\n"
        for rel in self.rel_in:
            res += "\t" + self._rel_to_string(rel) + "\n"
        res += "REL_IN\n"
        for rel in self.rel_out:
            res += "\t" + self._rel_to_string(rel) + "\n"
        return res


def main():
    import logging
    import sys
    if len(sys.argv)==1:
        word = "manger"
    else:
        word = sys.argv[1]
    import dump_manager
    
    dm = dump_manager.DumpManager()
    res = dm.get_dump(word)
    if not res:
        return
    
    analyzer = DumpAnalyzer(word)
    analyzer.logger.setLevel(logging.DEBUG)
    # print(analyzer)
    # analyzer.__str__()

    print("Pos de '" + word + "' ?")
    tmp = analyzer.get_nodes_by_typename("n_pos")
    for x in tmp:
        print("\t", x)

    print("node n_data?")
    tmp = analyzer.get_nodes_by_typename("n_data")
    for x in tmp:
        print("\t", x)
        
    print("rel n° 12345 '" + word + "' ?")
    tmp = analyzer.get_rels_by_type(12345)
    for x in tmp:
        print("\t", x)

    rels_a_test = ["r_adj-verbe", "r_verbe-adj",
                   # "r_associated",
                   "r_isA",
                   "r_family",
                   "r_lemma",
                   "r_verbe-action", "r_action-verbe",
                   "r_agentif_role",
                   "r_action_lieu", "r_lieu_action",
                   "r_lieu-1", "r_agent-1",
                   "r_nomprop-adj", "r_nomprop-adj",
                   "r_nomprop-adv", "r_nomprop-adv",
                   "r_adj-adv", "r_adv-adj",
    ]
    print("relations jugées intéressantes")
    for relname in rels_a_test:
        if not relname in analyzer.rel_dict.keys():
            continue
        print("  " + relname)
        tmp = analyzer.get_rels_by_typename(relname, incoming=True)
        for x in tmp:
            print("    in:\t", analyzer._rel_to_string(x))
        tmp = analyzer.get_rels_by_typename(relname, incoming=False)
        for x in tmp:
            print("    out:", analyzer._rel_to_string(x))
            
    # print(analyzer.get_rels_by_type(43, incoming=False))
    # print(analyzer)
if __name__ == '__main__':
    main()

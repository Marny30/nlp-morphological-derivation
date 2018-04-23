#!/usr/bin/python3
# -*- coding: utf-8 -*-

from transformation import TaggedWord, Rule
# from typing import List
import config
import dump_analyzer_factory

class ConstraintCheckException(Exception):
    pass

class ProductionChecker(config.Loggable):
    dump_factory = dump_analyzer_factory.Dump_analyzer_factory()
    
    def __init__(self, word_in, Rule, word_out):
        super().__init__()
        self.logger.info("Test transformation " + word_in + "-->" + word_out + " [" + Rule.commentaire+ "]")
        self.word_in = word_in
        self.Rule = Rule
        self.word_out = word_out
        
    def _check_nodeconstraint(self, analyzer, constraint):
        relname, labelconstraint = constraint.split()
        listnodes = analyzer.get_nodes_by_typename(relname)
        for node in listnodes:
            # self.logger.debug(node)
            if labelconstraint==node.label:
                self.logger.info('Contrainte "' + constraint + '" vérifiée.')
                return True
        self.logger.info('Contrainte "' + constraint + '" non vérifiée.')
        return False

    def _check_relconstraint(self, analyzer, word, constraint):
        
        node1label, relname, node2label = constraint.split()
        # Word vers otherword
        if node1label == 'X':
            node1label = self.word_in
        elif node1label == 'Y':
            node1label = self.word_out
        if node2label == 'X':
            node2label = self.word_in
        elif node2label == 'Y':
            node2label = self.word_out
        
        listrels = set()
        listrels.update(analyzer.get_rels_by_typename(relname, incoming=True))
        listrels.update(analyzer.get_rels_by_typename(relname, incoming=False))
        # Dans les deux sens!
        listrels = list(listrels)

        self.logger.info('Requete réécrite en ' + node1label + ' ' +relname +' ' +node2label)
        for rel in listrels:
            relnode1label = analyzer.get_node_by_id(rel.node1).label
            relnode2label = analyzer.get_node_by_id(rel.node2).label
            # self.logger.info(analyzer._rel_to_string(rel))
            # self.logger.info(relnode1label + " " + relnode2label)
            if relnode1label == node1label and relnode2label == node2label:
                self.logger.info('Contrainte "' + constraint + '" vérifiée.')
                return True
        self.logger.info('Contrainte "' + constraint + '" non vérifiée.')
        return False
        
    def _check(self, word, constraint_list, otherword):
        analyzer = ProductionChecker.dump_factory.create(word)
        if not analyzer:
            self.logger.warning("Le mot " + str(word) + " n'existe pas dans JDM")
            raise LookupError('mot inexistant dans JDM')
        
        for constraint in constraint_list:
            self.logger.debug("Traitement de la contrainte " + str(constraint))
            # relname, elem = constraint.split()
            tokens = constraint.split()
            if len(tokens)==2 and tokens[0].startswith('n_'):  # node (relname, elem)
            # if relname.startswith('n_'):
                if not self._check_nodeconstraint(analyzer, constraint):
                    raise ConstraintCheckException('Contrainte noeud "' + constraint + '" non vérifiée.')
            elif len(tokens)==3 and tokens[1].startswith('r_'):  # rel (node1 label, relname, node2 label)
                if not self._check_relconstraint(analyzer, word, constraint):
                    raise ConstraintCheckException('Contrainte rel "' + constraint + '" non vérifiée.')
            else:
                raise SyntaxError('type de contrainte inconnue')
        return True
        
    def check(self):
        # self.logger.debug("Check input")
        try:
            self._check(self.word_in, self.Rule.input_contrainte, self.word_out)
        except Exception as e:
            raise e
        
        try:
            self._check(self.word_out, self.Rule.output_contrainte, self.word_in)
        except Exception as e:
            raise e

        self.logger.info("transformation validée")
        return True
        
def main():
    import sys
    import dump_analyzer_factory
    # from parser import parseRule
    if len(sys.argv)==1:
        word = "changer"
    else:
        word = sys.argv[1]
    rulestr = "(.*)er=>\1euse ; 'Ver vers agent' (exemple : chanter => chanteuse);nom:infinitif;nom:agent"
    # rule = parseRule(rulestr)
    # rule = Rule("“Ver vers agent” (exemple : chanter => chanteuse)","(.*)er","\\1euse", ["n_pos Ver:Inf"],["n_pos Nom:Fem+SG"])
    # word_in = "chanter"
    # word_out = rule.production(TaggedWord("chanter","Ver:Inf"))

        # exemple jardin => jardinier #########################################
    # rule = Rule("'blablabla' (exemple : jardin => jardinier)","(.*)in","\\1inier", ["n_pos Nom:Mas+SG"],["n_pos Nom:Mas+SG", "X r_lieu-1 Y"])

    # word_in = "jardin"
    # word_out = rule.production(TaggedWord("jardin","Nom:Mas+SG"))
    # word_out = word_out.word

        # exemple frapper => frappement ########################################
    rule = Rule("'blablabla' (exemple : frapper => frappement)","(.*)er","\\1ement", ["n_pos Ver:Inf"],["n_pos Nom:Mas+SG", "Y r_lemma X"])

    word_in = "frapper"
    word_out = rule.production(TaggedWord("frapper","Nom:Mas+SG"))
    word_out = word_out.word
    
    checker = ProductionChecker(word_in, rule, word_out)
    if checker.check():
        print("ok!")
    else:
        print("pb")
    
if __name__ == '__main__':
    main()

    

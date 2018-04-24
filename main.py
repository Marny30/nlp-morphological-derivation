#!/usr/bin/python3
# -*- coding: utf-8 -*-

import parser
from constraint_checker import ProductionChecker


def showstats(stats):
    def triplet_to_str(triplet):
        return '{:<15} --[{:<80}]--> {:>15}'.format(triplet[0], triplet[1], triplet[2])
    
    print("Productions:",stats['productions'])
    print("Productions correctes : ", stats['right_production_number'])
    for prod in stats['right_productions']:
        print("\t",triplet_to_str(prod))
    print()
    print("Productions incorrectes : ", stats['wrong_production_number'])
    print("  Mots inexistants : ", len(stats['wrong_productions_not_found']))
    for prod in stats['wrong_productions_not_found']:
        print("\t",triplet_to_str(prod), ":", prod[3])
    print("  Autre :", len(stats['wrong_productions_not_constraint']))
    for prod in stats['wrong_productions_not_constraint']:
        print("\t",triplet_to_str(prod), ":", prod[3])
    print()
    print("Proportion de bonne production : ", round(stats['right_production_number']/ stats['productions']*100,3), '%')

def main():
    import logging
    
    triplets = parser.production()
    triplets = parser.production_label(triplets)

    stats = {'productions': len(triplets),
             'right_productions' : [],
             'right_production_number':0,
             'wrong_productions': [],
             'wrong_productions_not_found' : [],
             'wrong_productions_not_constraint' : [],
             'wrong_production_number':0,
    }
    word_n = len(triplets)

    for triplet in triplets:
        word_in, rule, production = triplet
        # print(type(rule.input_contrainte))
        checker = ProductionChecker(word_in, rule, production)
        try:
            checker.check()
            stats['right_productions'].append([word_in, rule.commentaire, production])
            stats['right_production_number'] += 1
        except Exception as e:
            stats['wrong_productions'].append([word_in, rule.commentaire, production, e])
            if isinstance(e, LookupError):
                stats['wrong_productions_not_found'].append([word_in, rule.commentaire, production, e])
            else:
                stats['wrong_productions_not_constraint'].append([word_in, rule.commentaire, production, e])
            stats['wrong_production_number'] += 1
    print()
    showstats(stats)
    
if __name__ == '__main__':
    main()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import parser
from constraint_checker import ProductionChecker 
def main():
    triplets = parser.production()
    triplets = parser.production_label(triplets)

    stats = {'right_production_number': 0, 'productions': len(triplets), 'wrong_production_number':0}
    word_n = len(triplets)

    for triplet in triplets:
        word_in, rule, production = triplet
        # print(type(rule.input_contrainte))
        checker = ProductionChecker(word_in, rule, production)
        if checker.check():
            stats['right_production_number'] += 1
        else:
            stats['wrong_production_number'] += 1
    print(stats)
    
if __name__ == '__main__':
    main()

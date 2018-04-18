#!/usr/bin/python3
# -*- coding: utf-8 -*-
from transformation import Rule, TaggedWord

list_rule=list()
list_word=list()
def parseRule(line):
    tokens = line.split(";")
    ru= tokens[1].split("=>")

    list_contrainte_in=list()
    crt=tokens[3].split(",")
    for r in crt:
        list_contrainte_in.append(r)

    list_contrainte_out=list()
    crts=tokens[4].split(",")
    for r1 in crts:
        list_contrainte_out.append(r1)

    return Rule(tokens[2],ru[0],ru[1], list_contrainte_in, list_contrainte_out)
    # n_pos Nom:Mas+SG", "Y r_lemma X
    
def parseWord(line):
    tokens = line.split(";")
    return TaggedWord(tokens[1], tokens[2])

def parse_file():
 PATH = "./jdm"
 with open(PATH, "r") as myfile:
     fichier=myfile.read()
     lignes = fichier.split("\n")
     for line in lignes: 
      #print(line)
     # print(" devient ")      
      tokens =line.split(";")
      if(tokens[0]== "RULE"):
      	list_rule.append(parseRule(line))
      elif tokens[0]== "WORD":      
        list_word.append(parseWord(line))
 return [list_rule,list_word]

def production():
    list_melanger = list()
    list_melanger = parse_file()
    list_rule=list_melanger[0]
    list_word=list_melanger[1]
    liste_triplet_production = list()
    for word in list_word:	
        for rule in list_rule:
            if rule.isAppliable(word):
                # if doublon(word,list_word) == False:
                liste_triplet_production.append([word, rule, rule.production(word)])
    return liste_triplet_production


def production_label(list_triplet_production):
    return_list= list()
        # print(triplet[0].word)
    for triplet in list_triplet_production:
        return_list.append([triplet[0].word,triplet[1],triplet[2].word])
    return return_list


def doublon(word,list_word):
   for w in list_word:
     if w == word:
       return True
   return False	

def find_word(word,liste_triplet_production):
    liste_triplet_find =list() 	
    # print("word", word)
    # print("1ermot")	
    for triplet in liste_triplet_production:
         print("triplet[0]", str(triplet[0]))
         if word == triplet[0].word:
             liste_triplet_find.append(triplet)
    return liste_triplet_find
	
def main():   
   triplet= production()
    
   marin=production_label(triplet)
   print("je marche")
   for m in marin:
       print(str(m))
   #     print(m[1])
   #     print(m[2])
   
if __name__ == '__main__':
    main()

#!/usr/bin/python3

from transformation import Rule, TaggedWord

list_rule=list()
list_word=list()
def parseRule(line):
    tokens = line.split(";")
    ru= tokens[1].split("=>") 
    return Rule(tokens[2],ru[0],ru[1],tokens[3],tokens[4])
    
def parseWord(line):
    tokens = tokens = line.split(";")
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
 print("Fichier parsé sans erreur")
 return [list_rule,list_word]


def main():   
    list_melanger =list()
    list_melanger =parse_file()
    list_rule=list_melanger[0]
    list_word=list_melanger[1]
   
    for word in list_word:	
        for rule in list_rule:
           if rule.isAppliable(word):
              list_word.append(rule.production(word))	        


if __name__ == '__main__':
    main()

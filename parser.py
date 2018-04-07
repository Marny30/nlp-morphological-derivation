#!/usr/bin/python3

from transformation import Rule, TaggedWord

def parseRule(line):
    tokens = line.split(";")
    return Rule(tokens[1], tokens[3], tokens[2], tokens[4])
    
def parseWord(line):
    tokens = tokens = line.split(";")
    return TaggedWord(tokens[1], tokens[2])

def main():
    PATH = "./rules_sufix"
    with open(PATH, "r") as myfile:
     fichier=myfile.read()
     lignes = fichier.split("\n")
    for line in lignes: 
      print(line)
      print(" devient ")      
      tokens =line.split(";")
      
      if(tokens[0]== "RULE"):
      	parseRule(line)
      else:	      
        parseWord(line)
      print("Fichier parsé sans erreur")
        
if __name__ == '__main__':
    main()

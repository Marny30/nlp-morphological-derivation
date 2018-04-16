#!/usr/bin/python3

from transformation import Rule, TaggedWord

def parseRule(line):
    tokens = line.split(";")
    ru= tokens[1].split("=>") 
    return Rule(tokens[2],ru[0],ru[1],tokens[3],tokens[4])
    
def parseWord(line):
    tokens = tokens = line.split(";")
    return TaggedWord(tokens[1], tokens[2])

def main():
    PATH = "./jdm"
    with open(PATH, "r") as myfile:
     fichier=myfile.read()
     lignes = fichier.split("\n")
     for line in lignes: 
      print(line)
      print(" devient ")      
      tokens =line.split(";")
      if(tokens[0]== "RULE"):
      	parseRule(line)
      elif tokens[0]== "WORD":      
        parseWord(line)
      print("Fichier parsé sans erreur")
        
if __name__ == '__main__':
    main()

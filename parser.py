#!/usr/bin/python3

from transformation import Rule, TaggedWord

def parseRule(line):
    tokens = line.split(";")
    return Rule(tokens[0], tokens[1], tokens[2], tokens[3])
    
def parseWord(line):
    tokens = tokens = line.split(";")
    return TaggedWord(tokens[0], tokens[1])

def main():
    PATH = "./exemple.txt"
    with open(PATH, "r") as myfile:
        print("TODO")
        # line = myfile.readline()
        # print(line)
        # print(" devient ")
        # print(parseLine(line))
        # print()
    print("Fichier parsé sans erreur")
        
if __name__ == '__main__':
    main()

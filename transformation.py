#!/usr/bin/python3

import re


class TaggedWord():
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos          # classe grammaticale
    def __str__(self):
        return self.word+"[" + self.pos + "]"

class Rule():
    ''' Règle de transformation de mot vers un autre '''
    def __init__(self, commentaire, input_regex, output_regex,input_contrainte,output_contrainte):
        self.commentaire = commentaire
        self.input_regex = input_regex
        self.output_regex = output_regex
        self.input_contrainte = input_contrainte
        self.output_contrainte = output_contrainte

    def isAppliable(self, taggedword):
        print(taggedword.pos)
        print(self.input_contrainte)
        print(self.input_regex)
        print(taggedword.word)
        return (taggedword.pos == self.input_contrainte
                and (re.match(self.input_regex, taggedword.word) is not None))

    def production(self, taggedword):      
        regex=re.sub(self.input_regex,self.output_regex, taggedword.word)
        return TaggedWord(regex, self.output_contrainte)	  

#RULE;(.*)’er’=>\1’euse’ ; “Ver vers agent” (exemple : chanter => chanteuse);nom:infinitif;nom:agent
def main():
    mot_exemple = TaggedWord("manger", "Ver:infinitif")
    regle_exemple = Rule("“Ver vers agent” (exemple : chanter => chanteuse)","(.*)er","\\1euse", "Ver:infinitif","nom:agent")
    	
    print("La règle est elle applicable sur", mot_exemple, "?")
    print(regle_exemple.isAppliable(mot_exemple))
    print("Production:")
    print(regle_exemple.production(mot_exemple))

if __name__ == "__main__":
    main()

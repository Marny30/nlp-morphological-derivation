#!/usr/bin/python3

import re

class TaggedWord():
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos          # classe grammaticale
    def __str__(self):
        return self.word+"[" + self.pos + "]"

# class RuleFactory():
#     def __init__(str)


class Rule():
    ''' Règle de transformation de mot vers un autre '''
    def __init__(self, input_pos, output_pos, input_regex, output_regex):
        self.input_pos = input_pos
        self.output_pos = output_pos
        self.input_regex = input_regex
        self.output_regex = output_regex
        
    def _parse(self, string):
        tokens = string.split(";")
        
        
    def isAppliable(self, mot):
        '''Renvoie vrai si la règle est applicable sur le mot renseigné. Il
        s'agit de vérifier que le mot aie (1) la classe grammaticale
        attendue et (2) que la forme du mot match avec le regex
        attendu
        '''
        return (mot.pos == self.input_pos
                and (re.match(self.input_regex, mot.word) is not None))

    def production(self, taggedword):
        import re
        # newstring = re.sub('(Banana)', r'\1Toothpaste', oldstring)
        return re.sub(self.input_regex, self.output_regex, taggedword.word)

    # def productions(self, taggedwords):
    #     res = []
    #     for m in taggedwords:
    #         if self.isAppliable(m):
    #             res += [self.production(m.word)]
    #     return res

def main():
    mot_exemple = TaggedWord("manger", "VERBE_1er_groupe")
                    # TaggedWord("braquer", "VERBE_1er_groupe")
    regle_exemple = Rule("VERBE_1er_groupe", "NOM", "(.*)er", "\\1eable")
    print("La règle est elle applicable sur", mot_exemple, "?")
    print(regle_exemple.isAppliable(mot_exemple))
    print("Production:")
    print(regle_exemple.production(mot_exemple))

if __name__ == "__main__":
    main()

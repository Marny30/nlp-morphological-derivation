#!/usr/bin/python3


class TaggedWord():
    def __init__(self, word, pos):
        self.word = word
        self.pos = pos          # classe grammaticale
    def __str__(self):
        return self.word+"[" + self.pos + "]"

class Rule():
    ''' Règle de transformation de mot vers un autre '''
    def __init__(self, string):
        ''' Definition par parsing '''
        tokens = string.split(";")
        self.input_pos = tokens[0]
        self.output_pos = tokens[1]
        self.input_regex = tokens[2]
        self.output_regex = tokens[3]

    def isAppliable(self, mot):
        '''Renvoie vrai si la règle est applicable sur le mot renseigné. Il
        s'agit de vérifier que le mot aie (1) la classe grammaticale
        attendue et (2) que la forme du mot match avec le regex
        attendu
        '''
        pass                    # TODO

    def production(self, taggedword):
        import re
        # newstring = re.sub('(Banana)', r'\1Toothpaste', oldstring)
        return re.sub(self.input_regex, self.output_regex, taggedword.word)

    def productions(self, taggedword):
        res = []
        for m in taggedword:
            if self.isAppliable(m):
                res += [self.production(m.word)]
        return res

def main():
    print("Hello world")

if __name__ == "__main__":
    main()

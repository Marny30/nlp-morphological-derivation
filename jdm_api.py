#!/usr/bin/python3

# http://www.jeuxdemots.org/rezo-dump.php
# dep : pip3 install --user beautifulsoup4

class DumpManager():
    def __init__(self):
        import os
        self.path = "./dumps/"
        self.localdumps = os.listdir(self.path)

    def _getHTML(self, link):
        import urllib.request
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        return the_page

    def _extract_dump_from_html(self,html_txt):
        import bs4
        soup = bs4.BeautifulSoup(html_txt, 'html.parser')
        res = ""
        try:
            res = soup.findAll('code')[0].get_text()
        except:
            raise ValueError('Mot non trouvable')
        return res

    def download_dump(self, mot):
        '''Téléchargement le dump JeuxDeMots d'un mot donné. Si le mot
        n'existe pas, la fonction renvoie une chaîne vide
        '''
        url = "http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel="+mot+"&rel="
        txt = self._getHTML(url)
        res = ""
        try:
            res = self._extract_dump_from_html(txt)
        except ValueError as verror:
            print(str(verror) + ": " + mot)
        return res

    def get_dump(self, mot):
        '''Récupère le dump d'un mot donné par JeuxDeMots. Il est d'abord
        éssayé d'obtenir ce dump localement, et s'il n'est pas stocké
        localement alors on le télécharge et on l'enregistre en local pour par
        la suite ne pas surcharger le serveur.
        '''
        pathmot = self.path + mot
        if mot in self.localdumps:  # Le dump est stocké en local
            with open(pathmot, "r") as dumpfile:
                res = dumpfile.read()
        else:                   # Le dump n'est pas stocké en local
            res = self.download_dump(mot)
            # enregistrement en local du dump s'il en existe un
            if res != '':
                with open(pathmot, "w") as dumpfile:
                    dumpfile.write(res)
                self.localdumps += [mot]
        return res

    def has_dump(self, mot):
        '''Renvoie vrai si un mot existe dans la base de donnée JeuxDeMots,
        faux sinon
        '''
        if mot in self.localdumps:
            return True
        else:
            dump = self.get_dump(mot)
            if dump != '':
                return True
        return False

def main():
    ''' Exemple '''
    dm = DumpManager()
    mots_a_tester = ["truc", "ordinateur", "QSDF"]
    for mot in mots_a_tester:
        print("Est-ce que le mot ", mot, " existe?")
        print(dm.has_dump(mot))
        print()
    print("Quel est le dump du mot 'lea'? (tronqué à 1000 caractères)")
    print(dm.get_dump('lea')[:1000])

if __name__ == '__main__':
    main()

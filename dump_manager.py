#!/usr/bin/python3
# -*- coding: utf-8 -*-

# http://www.jeuxdemots.org/rezo-dump.php
# dep : pip3 install --user beautifulsoup4


import config

class DumpManager(config.Loggable):
    def __init__(self):
        super(DumpManager, self).__init__()
        import os
        self.localdumps = os.listdir(config.DUMP_PATH)

    def _getHTML(self, link):
        import urllib.request
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        return the_page

    def _extract_dump_from_html(self, html_txt):
        import bs4
        soup = bs4.BeautifulSoup(html_txt, 'html.parser')
        res = ""
        try:
            res = soup.findAll('code')[0].get_text()
        except:
            raise ValueError('Dump inexistant')
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
            self.logger.debug(str(verror) + ": '" + mot +"'")
        return res

    def get_dump(self, mot):
        '''Récupère le dump d'un mot donné par JeuxDeMots. Il est d'abord
        éssayé d'obtenir ce dump localement, et s'il n'est pas stocké
        localement alors on le télécharge et on l'enregistre en local pour par
        la suite ne pas surcharger le serveur.
        '''
        pathmot = config.DUMP_PATH + mot
        self.logger.debug("Tentative d'obtention du dump associé à '"+str(mot)+"'")
        if mot in self.localdumps:  # Le dump est stocké en local
            self.logger.info("Dump '"+str(mot)+"' stocké localement."
                                     +" Lecture du fichier.")
            with open(pathmot, "r") as dumpfile:
                res = dumpfile.read()
        else:                   # Le dump n'est pas stocké en local
            self.logger.debug("Dump '"+str(mot)+"' Absent des dumps "
                                     + "locaux. Tentative de téléchargement.")
            res = self.download_dump(mot)
            # enregistrement en local du dump s'il en existe un
            if res != '':
                self.logger.debug("Dump '"+str(mot)+"' téléchargé. Enregistrement en local")
                with open(pathmot, "w") as dumpfile:
                    dumpfile.write(res)
                self.localdumps += [mot]
        return res

    def has_dump(self, mot):
        '''Renvoie vrai si un mot existe dans la base de donnée JeuxDeMots,
        faux sinon
        '''
        return self.get_dump(mot)!=''

def main():
    ''' Exemple '''
    import logging
    import sys
    if len(sys.argv)==1:
        mots_a_tester = ["changer", "changeable"]
    else:
        mots_a_tester = [sys.argv[1]]
        
    dump_manager = DumpManager()
    dump_manager.logger.setLevel(logging.DEBUG)
    for mot in mots_a_tester:
        print("Est-ce que le mot '" +mot+ "' existe?")
        print(dump_manager.has_dump(mot))
        print()
    # print("Quel est le dump du mot 'lea'? (tronqué à 1000 caractères)")
    # print(dm.get_dump('lea')[:1000])

if __name__ == '__main__':
    main()

# Description

Ce projet permet de générer, depuis le réseau lexical JDM et un ensemble de
règles, de générer de nouveaux mots et d'en vérifier la sémantique et la classe
grammaticale.

Le fichier de règles se trouve dans `./regles`, lesquelles sont en regex. Ce
projet s'étant basé sur JDM, une API python a dû être établie pour celui-ci.
Elle télécharge les dumps associés aux termes, les parse et les analyses. Un
terme est mis en cache une fois connu, de manière à ne pas sursolliciter le
serveur en le retéléchargeant plusieurs fois.

# Description de l'API
- `dump_manager.py` gère le téléchargement et la mise en cache des dumps
- `dump_parser.` parse le dump
- `dump_analyzer.py` permet l'extraction d'informations jugées intéressantes
- `dump_analyzer_adaptater.py` (qui n'est au final pas utilisé) permet
  l'extraction d'information de la même manière, mais avec des
  fonctions de plus haut niveau.
- `dump_analyzer_factory.py` permet l'instanciation de `dump_analyzers`.

# Comment utiliser
Éxécuter ```./main.py```

# Dépendences
- BeautifulSoup4 (pour parser, au travers de l'API)

# Modification après revu prof
- Mise en commentaire des règles de conjugaison

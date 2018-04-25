# Description
Ce projet permet de générer des dérivations morphologiques de mots à
partir d'un ensemble de règles et de mots donnés (voir
`./regles`). Les motifs de transformations sont écrits en regex, et un
ensemble de contrainte est associé à celles-ci pour vérifier leur
sémantique et leur classes grammaticales.

Ce projet étant écrit en python, il a fallu réaliser une API pour
télécharger et mettre en cache les dumps de JDM. Tous les fichiers
relatifs à celle ci sont préfixés de ```dump_```.

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

# Modification après revue prof
- Mise en commentaire des règles de conjugaison

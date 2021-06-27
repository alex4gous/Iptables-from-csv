# Traduction EN
[Here the google traductor](https://translate.google.com/translate?hl=&sl=auto&tl=en&u=https%3A%2F%2Fgithub.com%2Falex4gous%2FIptables-from-csv&sandbox=1)

---

# Génération d'Iptables via un fichier csv sous Debian (avec les bonnes pratiques)

Grace à un fichier Excel (iptables-redaction.xlsx) qui aide à fluidifier l'écriture des iptables, nous sauvegarderons ce même fichier en CSV, puis via le fichier python projet06.py nous uploaderons les différentes règles automatiquement sur le PC/Serveur.

![alt text](https://raw.githubusercontent.com/alex4gous/Projet06-OC/main/git-Capture%20d%E2%80%99%C3%A9cran%202021-06-06%20155059.png)

## Installation

- Utiliser le package manager [pip](https://pip.pypa.io/en/stable/) pour installer csv et apt.

```bash
pip install csv
pip install apt
```

- Generer le fichier csv (à partir du fichier excel):

![alt text](https://raw.githubusercontent.com/alex4gous/Projet06-OC/main/git-Capture%20d%E2%80%99%C3%A9cran%202021-06-06%20153123.png)


## Utilisation

Lancement du script:
```bash
python3 projet06.py --file exemple.csv
```
Dans le fichier exemple.csv, ne pas oublier de mettre votre adresse ip. L'exemple.csv autorise une seule connexion en SSH vers un PC distant.

### Attention, le fichier csv est obligatoire !
```python
### Les imports
import apt
import subprocess, os
import sys
import csv
import argparse

parser = argparse.ArgumentParser(description="Generateur d'iptables")
parser.add_argument('-f','--file', help='Import du fichier csv', required=True)
args = vars(parser.parse_args())

# Ne pas oublier d'importer un fichier csv !
```

## Evolution du code
- Récupération des entetes permetants des ajouts (ou suppression) de certains arguments
- Supprimer les lignes vides du csv (qui peuvent faire planter)
- L'installation automatique n'est pas faite car ce script a été développer sous debian 10. Donc faire en sorte que le script soit lancé sur les différentes distributions serait un plus. Que les paquets (iptables, iptables-persistent) s'installent automatiquement serait un gros plus.

---

## Rappel iptables

```bash
iptables -L #Pour lister nos règles parefeu
iptables -F #Pour vider notre table de règle
```

![alt text](https://raw.githubusercontent.com/alex4gous/Projet06-OC/main/git-Capture%20d%E2%80%99%C3%A9cran%202021-06-06%20153005.png) 

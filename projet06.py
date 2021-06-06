#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""P6.py: Mise en place d'iptables à partir d'un fichier csv préconçu."""

__author__ = "Alexandre FOURGOUS"
__copyright__ = "Copyright 2021, Openclassrooms P6"
__credits__ = ["alexandre fourgous"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "alex4gous"
__email__ = "alexandre.fourgous@orange.fr"
__status__ = "Production"

# Exemples:
# python3 P6.py --file iptables.csv

### Les imports
import apt
import subprocess, os
import sys
import csv
import argparse



parser = argparse.ArgumentParser(description="Generateur d'iptables")
parser.add_argument('-f','--file', help='Import du fichier csv', required=True)
args = vars(parser.parse_args())
#print(args['file'])


### Requis
# python3 -m pip install python_iptables


# Etape 1
# On verifie si le service iptable existe
cache = apt.Cache()
cache.open()

# On vérifie que iptables est installé
if cache['iptables'].is_installed:
        pass
else:
        print("Il faut installer le paquet iptables")
        sys.exit(2)

# blablablabla
# Si possible installer le paquet en silent - avec input choix exit ou install paquet.
if cache['iptables-persistent'].is_installed:
        pass
else:
        print("Il faut installer le paquet iptables-persistent")
        sys.exit(2)
        #os.system("apt-get install iptables-persistent -y") alternative possible


# On vérifie qu'on est ROOT
if not os.getuid() == 0:
        print("Il faut etre root pour changer les iptables.")
        sys.exit(2)

# Etape 2
# On met la politique de iptable (les 3) ou (les 6) en accept

list_policy = ["FORWARD", "INPUT", "OUTPUT"]
#os.system('iptables --policy FORWARD DROP')
def policy_iptables(list_policy, politique):
        for policy in list_policy:
                os.system('iptables --policy ' + policy + ' ' + politique)

policy_iptables(list_policy, 'ACCEPT')


# Etape 3
# On clear les règles existantes
os.system('iptables -F')

# Etape 4a
# On del les 2 premieres lignes
# On delete deux lignes ici:
a_file = open(args['file'], "r")
lines = a_file.readlines()
a_file.close()
del lines[0]
# On supprimer la ligne 1
del lines[0]
# Puis la ligne 2
new_file = open("temp.csv", "w+")
for line in lines: # On écrit dans le fichier temp.csv sans les lignes 1 et 2
    new_file.write(line)
new_file.close()


# Etape 4b
 # On lit le csv:
  # Boucle ligne par ligne:
  ## ligne par ligne à partir de la 3eme ligne. Puisque la deuxieme ligne d'entete (les arguments qui seront utilisés aprés)
  ## sera utilisé pour les arguments. On organise la règle pour du shell / python si possible On execute la règle

parametre_du_tableau = ["Hostame", "From", "To", "Port", "Command", "-t", "-A", "--policy", "-p", "-d", "-s", "-i", "-o", "--dport", "--sport", "-m", "--ctstate", "-d", "--ipv4", "-j", "--to-destination"]


with open('temp.csv', newline='') as f:
     reader = csv.reader(f)
     for row in reader:
# Ajouter les paramètres aux valeurs non vide du tableau
# Vérifier si il y a des valeurs vides

           if row[5] != "":
              row[5] = parametre_du_tableau[5] + " " + row[5]
           if row[6] != "":
              row[6] = parametre_du_tableau[6] + " " + row[6]
           if row[7] != "":
              row[7] = parametre_du_tableau[7] + " " + row[7]
           if row[8] != "":
              row[8] = parametre_du_tableau[8] + " " + row[8]
           if row[9] != "":
              row[9] = parametre_du_tableau[9] + " " + row[9]
           if row[10] != "":
              row[10] = parametre_du_tableau[10] + " " + row[10]
           if row[11] != "":
              row[11] = parametre_du_tableau[11] + " " + row[11]
           if row[12] != "":
              row[12] = parametre_du_tableau[12] + " " + row[12]
           if row[13] != "":
              row[13] = parametre_du_tableau[13] + " " + row[13]
           if row[14] != "":
              row[14] = parametre_du_tableau[14] + " " + row[14]
           if row[15] != "":
              row[15] = parametre_du_tableau[15] + " " + row[15]
           if row[16] != "":
              row[16] = parametre_du_tableau[16] + " " + row[16]
           if row[17] != "":
              row[17] = parametre_du_tableau[17] + " " + row[17]
           if row[18] != "":
              row[18] = parametre_du_tableau[18] + " " + row[18]
           if row[19] != "":
              row[19] = parametre_du_tableau[19] + " " + row[19]
           if row[20] != "":
              row[20] = parametre_du_tableau[20] + " " + row[20]
           # à VOIR POUR FAIRE AUTREMENT
           os.system(" ".join(row[4:21]))


# A voir si on peut pas rajouter en paramètre le fichier iptables.csv (fait)
# Et supprimer les dernieres lignes "vides" du csv (non fait)

# Etape 5
# On met la politique de iptable (les 3) ou (les 6) en deny
# Je reprend la fonction de l'étape 2
policy_iptables(list_policy, 'DROP')


# Etape 6
# On sauvegarde la règle
# Grace au paquet iptables-persistent
os.system("iptables-save > /etc/iptables/rules.v4")

# Etape 7
# On supprime le fichier temp.csv
os.system("rm temp.csv")

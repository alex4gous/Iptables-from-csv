#!/usr/bin/env python3.8

##############################################################################
#																			 #
#								FIREWALL									 #
#																			 #
##############################################################################
########### Mise en place automatique d'iptables via fichier csv #############
##############################################################################

### Les imports

import sys
import subprocess, os
import apt


# Etape 1
	# On vérifie si le service iptable existe
cache = apt.Cache()
if cache['iptables'].is_installed:
	print("YES it's installed")
else:
	print("NO it's NOT installed")

subprocess.call(["sudo", "apt-get", "update"])
# Etape 2
	# On met la politique de iptable (les 3) ou (les 6) en accept

# Etape 3
	# On clear les règles existantes

# Etape 4
	# On lit le csv:
		### Boucle ligne par ligne:
			# ligne par ligne
			# à partir de la 3eme ligne. Puisque la deuxieme ligne d'entete (les arguments qui seront utilisés aprés) sera utilisé pour les arguments.
			# On organise la règle pour du shell / python si possible
			# On execute la règle

	

import subprocess, os
import csv

parametre_du_tableau = ["Hostame", "From", "To", "Port", "Command", "-t", "-A", "--policy", "-p", "-d", "-s", "-i", "-o", "--dport", "--sport", "-m", "--c$

with open('iptables.csv', newline='') as f:
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


		
			
# Etape 5
	# On met la politique de iptable (les 3) ou (les 6) en deny

# Etape 6
	# On sauvegarde la règle


# Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie
battery_level = int(input("Entrez le niveau de batterie actuel: "))

# Vérifiez si le niveau de charge est valide
if battery_level >= 0 and battery_level <= 100:
    print("Niveau de batterie accepté")
else:
    print("Erreur: niveau de charge invalide.\nEntrez un niveau de batterie entre 0 et 100 inclusivement.")

# Arrondir le pourcentage à la dizaine la plus proche
battery_level = round(battery_level/10)*10

# Calculer le nombre de barres
barre = "❚"
nbr_barres = int(battery_level/10)

# Afficher la représentation graphique de la charge de la batterie
espace = " "
nbr_espaces = 10-nbr_barres

print("[{0}{1}]".format(nbr_barres*barre, nbr_espaces*espace))

# Exemple d'utilisation :
# Si l'utilisateur entre 76, la sortie sera :
# [❚❚❚❚❚❚❚❚     ]
# 76%
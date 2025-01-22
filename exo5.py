import math

# Constante de gravité
g = 9.8

# Demander la vitesse initiale de la boule
# Demander la vitesse initiale de la boule

vi = float(input("Veuillez saisir la vitesse initiale de la boule (en m/s) : "))

# Demander l'angle de lancement

angle = float(input("Veuillez saisir l'angle de lancement (en degrés) : "))

# Convertir l'angle en radians

radians = angle * math.pi / 180

# Calculer la distance maximale en x

Distance = (vi ** 2 * math.sin(2 * radians)) / 9.8

# Afficher la distance maximale arrondie à 2 chiffres après la virgule

print(f"Pour une vitesse initiale de {vi} m/s et un angle de {angle} degrés")
print(f"La distance parcourue serait de {Distance:.2f} m")

# Exemple:
# Pour une vitesse initiale de 10 m/s et un angle de 45 degrés
# La distance parcourue serait de 10.20m

import math 
secondes_totales = int(input("Entrez un nombre de secondes : "))

# Ne pas modifier.
annees = semaines = jours = heures = minutes = 0

# TODO: Assigner à la variable "annees" le nombre d'années
annees_completes = secondes_totales/60/60/24/365
annees = math.trunc(annees_completes)
print(f"Le nombre d'années est de {annees}")

annees_restantes = annees_completes % 1

# TODO: Assigner à la variable "semaines" le nombre de semaines restantes
semaines_completes = annees_restantes*365/7
semaines = math.trunc(semaines_completes)
print(f"Le nombre de semaines est de {semaines}")

semaines_restantes = semaines_completes % 1

# TODO: Assigner à la variable "jours" le nombre de jours restants
jours_complets = semaines_restantes*7
jours = math.trunc(jours_complets)
print(f"Le nombre de jours est de {jours}")

jours_restants = jours_complets % 1

# TODO: Assigner à la variable "heures" le nombre d'heures restantes
heures_completes = jours_restants*24
heures = math.trunc(heures_completes)
print(f"Le nombre d'heures est de {heures}")

heures_restantes = heures_completes % 1

# TODO: Assigner à la variable "minutes" le nombre de minutes restantes
minutes_completes = heures_restantes*60
minutes = math.trunc(minutes_completes)
print(f"Le nombre de minutes est de {minutes}")

minutes_restantes = minutes_completes % 1

# TODO: Assigner à la variable "secondes" le nombre de secondes restantes
secondes = round(minutes_restantes*60, 2)
print(f"Le nombre de secondes est de {secondes}")

# TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
# Exemple: print(annees, semaines, jours, heures, minutes, secondes_completes)
print("Le nombre de secondes {0} équivaut à {1} années, {2} semaines, {3} jours, {4} heures, {5} minutes et {6} secondes".format(secondes_totales, annees, semaines, jours, heures, minutes, secondes)) 
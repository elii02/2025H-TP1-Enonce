import math

a = int(input("Entrez a, non nul: "))
b = int(input("Entrez b: "))
c = int(input("Entrez c: "))

# Calculer le discriminant et assigner la valeur dans la variable "delta"
# delta = ...

delta = b ** 2 - 4 * a * c

# Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
# naPasDeSolution = ...
if delta < 0:
    naPasDeSolution = True
else:
    naPasDeSolution = False
    
if naPasDeSolution:
    # ces ligne de code seront executé si il y'a aucune racine
    # afficher sur l'écran "Aucune racine"
    # print("Aucune racine")

    print("Pour a =", a, ", b =", b, "et c =", c)
    print("Aucune racine")

    pass
else:
    # Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    # aUneSeuleSolution = ...

    if delta == 0:
        aUneSeuleSolution = True
    else:
        aUneSeuleSolution = False

    if aUneSeuleSolution:
        # ces ligne de code seront executé si il y'a une seule racine
        # afficher sur l'écran "Une seule racine"
        # print("Une seule racine")
        # assigner a la variable x1 la valeur de la racine
        # x1 = ...
        # print(x1)

        x1 = -b / (2 * a)

        print("Pour a =", a, ", b =", b, "et c =", c)
        print(delta)
        print("Une seule racine")
        print("x1 =", x1)

        pass
    else:
        # Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
        # aDeuxSolutions = ...

        aDeuxSolutions = True

        if aDeuxSolutions:
            # afficher sur l'écran "Deux racines"
            # print("Deux racines")
            # calculer la prmiere racine, assigner la a "x1"
            # x1 = ...
            # calculer la deuxieme racine, assigner la a "x2"
            # x2 = ...
            # print(x1, x2)

            x1 = round((-b + math.sqrt(delta)) / (2 * a), 2)
            x2 = round((-b - math.sqrt(delta)) / (2 * a), 2)

            print("Pour a =", a, ", b =", b, "et c =", c)
            print(delta)
            print("Deux racines")
            print("x1 =", x1, ", x2 =", x2)
            pass

# Exemple d'utilisation:
# Pour a = 1, b = -3, c = 2
# delta = 1
# Deux racines
# x1 = 1.0, x2 = 2.0

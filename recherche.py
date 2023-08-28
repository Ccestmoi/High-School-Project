# Créé par florian, le 12/12/2021 en Python 3.7

tab = [27, 13, 5, 1, 26, 4, 8, 23, 11]

valeur = int(input("Nombre recherché: "))
i = 0
trouve = False
while i < len(tab) and trouve == False:
    if tab[i] == valeur:
        trouve = True
        print("Le nombre", valeur, "est dans le tableau.")
    else:
        i = i + 1

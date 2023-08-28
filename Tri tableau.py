# Créé le 15/11/2021 en Python 3.7


# Saisie du tableau
def Saisie_Tableau():
    # Demander la longueur du tableau
    longueurTableau = input("Saisissez la longueur du tableau: ")
    # Gestion d'erreur de la longueur du tableau
    test = True
    while test:
        try:
            longueurTableau = int(longueurTableau)
            test = False
        except ValueError:
            print("Désolé, la valeur saisie n'est pas un nombre.")
            longueurTableau = input("Saisissez la longueur du tableau: ")
    # Entrée des valeurs du tableau
    Tableau = []
    for loop in range(longueurTableau):
        nombre = input("Saisissez les valeurs voulues: ")
        # Gestion d'erreur des valeurs voulues
        test = True
        while test:
            try:
                nombre = int(nombre)
                Tableau.append(nombre)
                test = False
            except ValueError:
                print("Saisissez un nombre décimal.")
                nombre = input("Saisissez les valeurs voulues: ")
        print(Tableau)
    return Tableau


# Fonction qui affiche le menu et retourne le choix
def Menu():
    # Définition d'un tuple pour affichage du menu
    Menu = ("1. Utiliser un nouveau tableau",
            "2. Utiliser le tri par insertion",
            "3. Utiliser le tri par selection",
            "0. Quitter")
    # Affichage du menu
    for i in Menu:
        print(i)
    # Demande du choix
    choix = input("Faites votre choix: ")
    # Gestion de l'erreur du choix dans le menu
    test = True
    while test:
        try:
            choix = int(choix)
            test = False
        except ValueError:
            print("Le choix doit être 0, 1, 2 ou 3.")
            choix = input("Faites votre choix: ")
    return choix


# Fonction de tri par insertion pour ranger les éléments d'un tableau
def Tri_Insertion(Tableau):
    j = 1
    # Boucle 1
    while j <= len(Tableau) - 1:
        i = j - 1
        k = Tableau[j]
        # Boucle 2
        while i > 0 - 1 and Tableau[i] > k:
            Tableau[i+1] = Tableau[i]
            i = i - 1
        Tableau[i + 1] = k
        print(Tableau)
        j = j + 1


# Fonction de tri par sélection pour ranger les éléments d'un tableau
def Tri_Selection(Tableau2):
    i = 0
    # Boucle 1
    while i < len(Tableau2) - 1:
        j = i + 1
        min = i
    # Boucle 2
        while j <= len(Tableau2) - 1:
            if Tableau2[j] < Tableau2[min]:
                min = j
            j = j + 1
        if min != i:
            Tableau2[i], Tableau2[min] = Tableau2[min], Tableau2[i]
        print(Tableau2)
        i = i + 1


def main():
    # Appel des variables de la fonction Saisie_Tableau
    Tableau = Saisie_Tableau()
    Tableau2 = Tableau.copy()
    # Initialisation de la valeur du choix pour entrer dans la boucle
    choix = -1
    # Boucle pour le menu
    while choix != 0:
        choix = Menu()
        if choix == 1:
            Tableau = Saisie_Tableau()
        elif choix == 2:
            Tri_Insertion(Tableau)
        elif choix == 3:
            Tri_Selection(Tableau2)
        elif choix != 0:
            print("Choix impossible")


main()

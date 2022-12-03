# Puissance 4 par Florian Bredow, Pruvost Alexis, Amara Korba Ihsan


def regles():
    regles = ["""
                              ┌─────────────┐
                              │ Puissance 4 │
                              └─────────────┘

                Les règles du puissance 4 sont des plus simples :

                Le joueur 1 a le pion ● , le joueur 2 a le pion ○ .
                Il faut poser un pion tour à tour en choisissant le
                numéro de colonne.
                Les numéros des colonnes sont de 1 à 7, de gauche à
                droite.
                Le premier à aligner 4 jetons horizontalement,
                verticalement ou en diagonale remporte la partie.
            """]
    print(regles[0])


# Fonction qui affiche le menu et retourne le choix
def Menu():
    # Définition d'un tuple pour affichage du menu
    Menu = ("\n1. Lancer une partie",
            "2. Règles du jeu",
            "0. Quitter")
    # Affichage du menu
    for i in Menu:
        print(i)
    # Demande du choix
    choix = input("Faites votre choix : ")
    # Gestion de l'erreur du choix dans le menu
    test = True
    while test:
        try:
            choix = int(choix)
            test = False
        except ValueError:
            print("Le choix doit être 0, 1 ou 2.")
            choix = input("Faites votre choix : ")
    return choix


# Fonction permettant d'avoir un tableau de grille de puissance 4 vierge
def tableau():
    '''La fonction est un tableau de tableau vierge. Celui sera retourné.'''
    tab = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " "]]

    return tab


# Fonction qui permet l'entrée du numéro de colonne
def Entree(tab, joueur):
    ''' La fontion sert à entrer un chiffre entre 1 et 7
    pour choisir la colonne où sera placé le jeton du joueur.
    Elle a comme entrée le tableau du jeu et le joueur qui joue. Et renvoie
    la colonne et la ligne du pion placé.'''
    i = 0
    test = False

    # Phrase pour indiquer le joueur qui doit jouer
    if joueur == 1:
        numero_colonne = input("\nJoueur 1 à votre tour (●), \
saisissez votre numéro de colonne : ")
    else:
        numero_colonne = input("\nJoueur 2 à votre tour (○), \
saisissez votre numéro de colonne : ")

    # Vérifie qu'un seul caractère est entré
    if len(numero_colonne) == 1:
        # Vérifie que le caractère entré est entre 1 et 7
        if ord("1") <= ord(numero_colonne) <= ord("7"):
            # Enlève 1 au chiffre entré pour l'utiliser comme indice de la
            # colonne dans la fonction Jeu
            chiffre = int(numero_colonne) - 1
            # Vérifie que la colonne choisie n'est pas pleine
            while i != 6 and test is False:
                # Vérifie que la case est vide
                if tab[chiffre][i] == ' ':
                    test = True
                    # Placement du pion dans la grille
                    if joueur == 1:
                        tab[chiffre][i] = "●"
                    else:
                        tab[chiffre][i] = "○"
                else:
                    i += 1
        else:
            print("Choisissez bien un chiffre entre 1 et 7 inclus.")
            return Entree(tab, joueur)
    else:
        print("Saisissez un seul chiffre.")
        return Entree(tab, joueur)
    # Vérifie le résultat de l'état de remplissage de la colonne
    if test is False:
        print("La colonne est pleine.")
        return Entree(tab, joueur)
    else:
        return chiffre, i


# Fonction qui permet de savoir à quel joueur est le tour
def Joueur(coups_joués):
    '''La fonction a comme entrée le nombre de coups joués dans la partie,
    elle va diviser par 2 ce nombre, si il reste 0, c'est le joueur 1, si
    il reste 1, c'est le joueur 2. Elle retourne le numéro du joueur.'''

    # Division euclidienne par 2 du nombre de coups joués
    if coups_joués % 2 == 0:
        joueur = 1
    else:
        joueur = 2
    return joueur


# Fonction permettant l'affichage d'une grille de puissance 4
def Affichage(tab):
    '''La fonction a le tableau comme entrée. Elle permet d'afficher le
    tableau sous forme d'une grille de puissance 4 et le numéro des colonnes
    au dessus.'''
    y = 5

    # Numéro des colonnes
    print("     1     2     3     4     5     6     7")
    print("     ↓     ↓     ↓     ↓     ↓     ↓     ↓")
    # Affichage de la grille
    print("  ╔═════╦═════╦═════╦═════╦═════╦═════╦═════╗")
    # Boucle pour l'affichage
    while y > 0:
        for i in range(7):
            print("  ║ ", tab[i][y], end='')
        print("  ║")
        print("  ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣")
        y = y - 1
    for i in range(7):
        print("  ║ ", tab[i][y], end='')
    print("  ║")
    print("  ╠═════╩═════╩═════╩═════╩═════╩═════╩═════╣")
    print("  ║                                         ║")
    print("──╨──                                     ──╨──")


# Fonction de vérification de l'alignement vertical des pions
def verif_verticale(colonne, ligne, tab):
    '''La fonction a comme entrée la colonne et la ligne du pion placé ainsi
    que le tableau. Elle va vérifier que les pions en dessous de celui qui est
    placé soient les mêmes que celui-ci. Elle va retourner le résultat de
    l'alignement.'''
    test = False
    c = colonne
    compteur = 0

    if ligne > 2:
        test2 = False
        l = ligne
        # Vérification de l'alignement des pions
        while test2 is False and l >= 1:
            # Comparaison des pions en dessous de celui qui est placé
            if tab[c][ligne] == tab[c][l-1]:
                compteur += 1
                l -= 1
            else:
                test2 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True
    return test


# Fonction de vérification de l'alignement horizontal des pions
def verif_horizontale(colonne, ligne, tab):
    '''La fonction a comme entrée la colonne et la ligne du pion placé ainsi
    que le tableau. Elle va vérifier que les pions à gauche de celui qui est
    placé soient les mêmes que celui-ci. Elle va faire de même avec ceux à
    droite. Puis elle va retourner le résultat de l'alignement.'''
    test = False
    l = ligne
    test2 = False
    c = colonne
    test3 = False
    c2 = colonne
    compteur = 0

    if 0 <= colonne <= 6:
        # Vérification de l'alignement des pions
        while test2 is False and c >= 1:
            # Comparaison des pions à gauche de celui qui est placé
            if tab[colonne][l] == tab[c-1][l]:
                compteur += 1
                c -= 1
            else:
                test2 = True
        # Vérification de l'alignement des pions
        while test3 is False and c2 <= 5:
            # Comparaison des pions à droite de celui qui est placé
            if tab[colonne][l] == tab[c2+1][l]:
                compteur += 1
                c2 += 1
            else:
                test3 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True

    return test


# Fonction de vérification de l'alignement en diagonale croissante des pions
def verif_diago_croissant(colonne, ligne, tab):
    '''La fonction a comme entrée la colonne et la ligne du pion placé ainsi
    que le tableau. Elle va vérifier que les pions en bas à gauche de celui qui
    est placé soient les mêmes que lui. Elle va faire de même avec ceux au
    dessus à droite. Puis elle va retourner le résultat de l'alignement.'''
    test = False
    test2 = False
    test3 = False
    l = ligne
    l2 = ligne
    c = colonne
    c2 = colonne
    compteur = 0

    if 0 <= colonne <= 6:
        # Vérification de l'alignement avec les pions en bas à gauche
        while test2 is False and c >= 1 and l >= 0:
            # Comparaison des pions avec celui qui est placé
            if tab[colonne][ligne] == tab[c-1][l-1]:
                compteur += 1
                c -= 1
                l -= 1
            else:
                test2 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True

    if 0 <= colonne <= 5 and 0 <= ligne <= 4:
        # Vérification de l'alignement avec les pions en bas à droite
        while test3 is False and c2 <= 5 and l2 <= 4:
            # Comparaison des pions avec celui qui est placé
            if tab[colonne][ligne] == tab[c2+1][l2+1]:
                compteur += 1
                c2 += 1
                l2 += 1
            else:
                test3 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True

    return test


# Fonction de vérification de l'alignement en diagonale décroissante des pions
def verif_diago_decroissant(colonne, ligne, tab):
    '''La fonction a comme entrée la colonne et la ligne du pion placé ainsi
    que le tableau. Elle va vérifier que les pions en bas à droite de celui qui
    est placé soient les mêmes que lui. Elle va faire de même avec ceux au
    dessus à gauche. Puis elle va retourner le résultat de l'alignement.'''
    test = False
    test2 = False
    test3 = False
    l = ligne
    l2 = ligne
    c = colonne
    c2 = colonne
    compteur = 0

    if 1 <= colonne <= 5 and 0 <= ligne <= 4:
        # Vérification de l'alignement avec les pions en haut à gauche
        while test2 is False and c >= 0 and l <= 4:
            # Comparaison des pions avec celui qui est placé
            if tab[colonne][ligne] == tab[c-1][l+1]:
                compteur += 1
                c -= 1
                l += 1
            else:
                test2 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True

    if 0 <= colonne <= 5 and 1 <= ligne <= 5:
        # Vérification de l'alignement avec les pions en bas à droite
        while test3 is False and c2 <= 5 and l2 >= 0:
            # Comparaison des pions avec celui qui est placé
            if tab[colonne][ligne] == tab[c2+1][l2-1]:
                compteur += 1
                c2 += 1
                l2 -= 1
            else:
                test3 = True
        # Confirmation de l'alignement des pions
        if compteur == 3:
            test = True

    return test


# Fonction qui permet le fonctionnement du jeu
def Jeu():
    '''La fonction sert au bon et harmonieux fonctionnement des fonctions
    pour le jeu. Elle est composée d'une boucle qui ne s'arrête que si un
    des joueurs a gagné ou que la grille soit pleine. La boucle commence par
    définir le joueur qui joue, puis le nombre total de coup joués va augmenter
    de 1, ensuite la fonction Entree va permettre d'avoir la colonne et la
    ligne du pion que le joueur aura placé, et s'en suit toutes les
    vérifications, en commençant par la vérification verticale, horizontale et
    des deux diagonales. Après cela, le tableau sera affiché sous forme de
    grille de puissance 4. Et pour finir, si l'une des vérifications retourne
    un alignement vrai, le jeu s'arrêtera.'''
    tab = tableau()
    Affichage(tab)
    coups_joués = 0
    victoire = False

    # Boucle pour le jeu
    while coups_joués != 42 and victoire is False:
        # Définition du joueur qui va jouer
        joueur = Joueur(coups_joués)
        coups_joués += 1
        # Obtention de la colonne et la ligne du pion placé par le joueur
        colonne, ligne = Entree(tab, joueur)
        # Vérifications de l'alignement
        verif1 = verif_verticale(colonne, ligne, tab)
        verif2 = verif_horizontale(colonne, ligne, tab)
        verif3 = verif_diago_croissant(colonne, ligne, tab)
        verif4 = verif_diago_decroissant(colonne, ligne, tab)
        # Affichage de la grille
        Affichage(tab)

        # Vérification de fin de jeu
        if verif1 is True:
            victoire = True
            print("Le joueur", joueur, "a gagné !")
        if verif2 is True:
            victoire = True
            print("Le joueur", joueur, "a gagné !")
        if verif3 is True:
            victoire = True
            print("Le joueur", joueur, "a gagné !")
        if verif4 is True:
            victoire = True
            print("Le joueur", joueur, "a gagné !")

    if coups_joués == 42:
        print("La grille est pleine, aucun coup n'est donc possible.")


def main():
    # Initialisation de la valeur du choix pour entrer dans la boucle
    choix = -1
    # Boucle pour le menu
    while choix != 0:
        choix = Menu()
        if choix == 1:
            Jeu()
        elif choix == 2:
            regles()
        elif choix != 0:
            print("Choix impossible.")

main()

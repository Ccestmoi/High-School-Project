# Créé par florian, le 26/01/2022 en Python 3.7

from random import choice


def regles():
    regles = ["""
                                Règles du jeu

                Les règles du jeu du pendu sont simples:
                    - Il faut trouver un mot choisi aléatoirement par
                      le programme et caché.
                    - 7 erreurs sont autorisées avant d'être pendu.
                    - Les lettres peuvent être entrées en majuscule ou en
                      minuscule et doivent être entrées une seule à la fois.
                    - Si une lettre a déjà éte entrée, vous en serez averti.
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
            print("Le choix doit être 0 ou 1.")
            choix = input("Faites votre choix : ")
    return choix


# Fonction pour importer les mots du fichier texte
def Import():
    '''Fonction qui importe les mots du fichier texte, qui va les stocker dans
    une liste en supprimant le \n qui est à la fin du mot.'''
    List = []
    # Import des mots du fichier dans une liste
    with open('mots.txt', "r") as fichier:
        for words in fichier:
            mots = words.replace('\n', '')
            List.append(mots)
    return List


# Fonction qui remplace le mot à trouver par des underscores
def Mot_caché(mot, L=[]):
    '''La fonction sert à mettre le mot dans une liste en remplaçant les lettres
    par des underscores.'''
    r = ''
    # Remplacement des lettres par des underscores
    # en fonction de la longueur du mot
    for lettre in mot:
        if lettre in L:
            r += lettre + ' '
        else:
            r += '_ '
    return r[:-1]


# Fonction d'entrée de la lettre
def Entrée():
    '''La fonction permet d'entrer les lettres que l'on veut, lorsqu'un caractère
    est entré, le programme vérifiera qu'il soit entre la valeur ASCII
    de la lettre A et de la lettre Z incluses, et le retournera en majuscule si
    la lettre est entrée en majuscule, si la lettre est en minuscule, elle sera
    retournée en majuscule. Si le caractère entré n'est pas une lettre,
    le programme redemandera une nouvelle entrée.'''
    # Entrée de la lettre par l'utilisateur
    lettre = input("Entrez une lettre : ")
    # Gestion d'erreur: vérifie que c'est une lettre majuscule ou minuscule
    try:
        if len(lettre) == 1 and ord("A") <= ord(lettre) <= ord("Z"):
            return lettre
        elif len(lettre) == 1 and ord("a") <= ord(lettre) <= ord("z"):
            return lettre.upper()
        else:
            return Entrée()
    except TypeError:
        return Entrée()


# Fonction qui affiche les étapes du pendu
def dessinPendu(nb):
    '''La fonction qui affiche le dessin du pendu en fonction de la valeur
    associé à la variable nb dans la fonction jeu.'''
    # Les "triples guillemets" """ permettent de délimiter une chaîne de
    # caractères située sur plusieurs lignes
    # (chaîne de caractères multi-lignes).
    tab = ["""
              +-------+
              |
              |
              |
              |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |
              |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |       |
              |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |      -|
              |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |      -|-
              |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |      -|-
              |      |
              |
           ==============
           """,
           """
              +-------+
              |       |
              |       O
              |      -|-
              |      | |
              |
           ==============
           """]
    print(tab[nb])


# Fonction qui permet le fonctionnement du jeu du pendu
def Jeu(mot):
    # Définition des variables nécessaires au fonctionnement du jeu
    lettre_mot = []
    affichage = Mot_caché(mot)
    print("Mot à trouver : ", affichage)
    nb = 0
    # Boucle qui permet de jouer jusqu'à ce que le nombre d'erreurs soit égal à
    # 7 et qu'il reste des undescore dans la variable affichage.
    while '_' in affichage and nb < 7:
        lettre = Entrée()
        if lettre not in lettre_mot:
            if lettre not in lettre_mot:
                lettre_mot += [lettre]
            if lettre not in mot:
                dessinPendu(nb)
                nb = nb + 1
            affichage = Mot_caché(mot, lettre_mot)
            print("Mot à deviner : ", affichage)
        else:
            print("Les lettres déjà entrées sont : ")
            print(*lettre_mot, sep=', ')
    if nb == 7:
        print("Le mot était : ", mot)
    elif '_' not in affichage:
        print("Vous avez trouvé le mot ! ")


def main():
    # Initialisation de la valeur du choix pour entrer dans la boucle
    choix = -1
    # Définition de la liste de mots
    List = Import()
    # Boucle pour le menu
    while choix != 0:
        choix = Menu()
        if choix == 1:
            mot = choice(List)
            Jeu(mot)
        elif choix == 2:
            regles()
        elif choix != 0:
            print("Choix impossible.")

main()

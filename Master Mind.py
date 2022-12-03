# Créé par Florian Bredow, le 18/03/2022 en Python 3.7

from random import randint
from operator import index


def regles():
    regles = ["""
                                Règles du jeu

                Les règles du Mastermind sont les suivantes:

                    - Il faut trouver un code choisi de manière aléatoire par
                      le programme.
                    - 10 codes peuvent être entrés avant de perdre.
                    - Les codes que vous entrez doivent être composés de 4
                      chiffres et sans espaces entre les chiffres.
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


# Fonction qui crée un code à 4 chiffres avec les chiffres entre 1 et 6
def Code_a_trouver():
    ''' Fonction qui génère un code avec 4 chiffres choisis aléatoirement entre
        1 et 6'''
    Code = []
    # Boucle qui ajoute 4 chiffres dans le tableau "Code"
    for i in range(4):
        chiffre = str(randint(1, 6))
        Code.append(chiffre)
    print(Code)
    return Code


# Fonction qui permet à l'utilisateur d'entrer des chiffres entre 1 et 6 pour
# trouver le code
def Entree():
    ''' La fontion sert à entrer des chiffres sous forme de code à 4 chiffres.
        Il faut entrer 4 chiffres entre ceux de 1 jusqu'à 6 sans espaces entre
        les chiffres. '''

    chiffre = str(input("Entrez votre code à 4 chiffes : "))
    Chiffres = []
    if len(chiffre) == 4:
        for i in chiffre:
            if ord("1") <= ord(i) <= ord("6"):
                Chiffres.append(i)
            else:
                print("Choisissez bien des chiffres entre 1 et 6 inclus.")
                return Entree()
    else:
        print("Saisissez 4 chiffres, ni plus ni moins.")
        return Entree()
    return Chiffres


# Fonction qui permet le fonctionnement du jeu
def Jeu():
    '''La fonction va comparer pour chaque élément dans le code à trouver 
    avec ceux dans le code entré, si le chiffre est présent et que l'index 
    est le même, il sera compté comme bon, si le chiffre est présent mais
    que les index ne correspondent pas, il sera compté comme mal placé.
    Si le chiffre n'est pas dans le code à trouver, il ne se passe rien.
    Toutes ces comparaisons se font jusqu'à ce que les 4 chiffres entrés 
    soient bons ou jusqu'à ce que 12 codes soient entrés.'''
    Code = Code_a_trouver()
    Deja_proposes = []
    essais = 0
    gagné = False

    while essais != 12 and gagné is False:
        Copy_Code = Code.copy()
        bons = 0
        bien_placé = 0
        mal_placé = 0
        Chiffres = Entree()
        Deja_proposes.append(''.join(Chiffres))

        for element in Copy_Code:
            if element in Chiffres:
                if Chiffres.index(element) == Copy_Code.index(element):
                    bien_placé += 1
                    bons = bons + 1
                elif Chiffres.index(element) != Copy_Code.index(element):
                    mal_placé += 1
        print("Bien placés : ",  bien_placé, "\nMal placés : ", mal_placé)
        if bons == 4:
            gagné = True
        else:
            print("\nCodes déjà proposés : ", ', '.join(Deja_proposes))
        essais = essais + 1

    if gagné is True:
        print("\nVous avez gagné !",
              "\nNombre d'essais : ", essais)
    else:
        print("Vous avez perdu.")


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

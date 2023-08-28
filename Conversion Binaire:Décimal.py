#menu
def menu():
    print("1. Binaire à décimal \n2. Décimal à binaire")
    choisir = int(input())
    if choisir == 1:
        print("")

    elif choisir == 2:
        print("")

menu()

#décimal en binaire
def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')
nbr = int(input("Entrez un nombre decimal : "))
conversion(nbr)


#binaire en décimal
def bindec():
    n = int(input("Entrez un nombre binaire : "))
    resultat = 0
    nbbinaire = str(n)
    liste = list(nbbinaire)
    exposant = len(liste)
    for nb in range(exposant):
      int(nb)
      ajout = int(liste[nb]) * 2 ** (exposant - 1 - nb)
      resultat = resultat + ajout
    print("Le nombre décimal est", resultat)
bindec()
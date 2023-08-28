# Créé par FlorianBREDOW, le 17/12/2021 en Python 3.7

tab = [1, 4, 5, 8, 11, 13, 23, 26, 27]
valeur = int(input())
trouve = False
d = 0
f = len(tab)

while f - d >= 1 and trouve == False:
    m = (d + f) // 2
    if valeur == tab[m]:
        trouve  = True
    elif tab[m] > valeur:
        f = m
    else:
        d = m

if trouve == True:
    print("Est dans le tableau.")
else:
    print("N'est pas dans le tableau.")

# Créé par florian, le 22/01/2022 en Python 3.7

Liste = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000,
    50000]
Liste2 = []
Rendu = int(input())
i = len(Liste) - 1

while Rendu != 0:
    if Liste[i] > Rendu:
        i = i - 1
    else:
        Rendu = Rendu - Liste[i]
        Liste2.append(Liste[i])
print(Liste2)

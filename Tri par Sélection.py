# Créé le 22/10/2021 en Python 3.7

def main():
    tab = [15,1,7,23,48]
    i = 0
    while i < len(tab) - 1:
        j = i + 1
        min = i
        while j <= len(tab) - 1:
            if tab[j] < tab[min]:
                min = j
            j = j + 1
        if min != i:
            tab[i], tab[min] = tab[min], tab[i]
        i = i + 1
    print(tab)

main()
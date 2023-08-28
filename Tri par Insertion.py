# Créé par florian, le 14/11/2021 en Python 3.7

t = [27, 10, 12, 8, 11]
j = 1
while j <= len(t) - 1:
    i = j -1
    k = t[j]
    while i > 0 - 1 and t[i] > k:
        t[i+1] = t[i]
        i = i - 1
    t[i + 1] = k
    j = j + 1
    print(t)

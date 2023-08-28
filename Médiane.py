# Créé par FlorianBREDOW, le 09/01/2022 en Python 3.7

t = [8, 12, 6, 24, 15, 1]

t.sort()
n = len(t)
if n%2 == 0:
    print((t[n//2-1] + t[n//2])/2)
else:
    print(t[(n-1)//2])
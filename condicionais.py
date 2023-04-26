import math
from statistics import median

n1 = 10.0
n2 = 10.0 
n3 = 10.0


# media = math.fsum([n1, n2, n3]) / 3
media = median([n1, n2, n3])

print(f"A média é:{round(media, 2)}")

if media < 6:
    print("Reprovado!")
elif media > 6 and media == 10:
    print("Aprovado com nota 10! Parabéns!")
else:
    print("Aprovado!")
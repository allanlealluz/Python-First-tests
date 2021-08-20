from random import randint
n1 = randint(1,10)
n2 = randint(1,10)
n3 = randint(1,10)
n4 = randint(1,10)
n5 = randint(1,10)

lista = (n1,n2,n3,n4,n5)
print(lista)
c = 0
menor = lista[0]
maior = lista[0]
while c < len(lista):
    if(lista[c] < menor):
        menor = lista[c]
        print(lista[c])
    if(lista[c] > maior):
        maior = lista[c]
        print(lista[c])
    c += 1
print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')

n1 = int(input('escreva um numero: '))
n2 = int(input('escreva outro numero: '))
n3 = int(input('escreva um ultimo numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior  = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print('o maior numero é {} e o menor numero é {}'.format(maior,menor))
print('\033[1:32:44m ola\033[m')
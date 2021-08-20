n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
n4 = int(input('digite um numero: '))
lista = (n1,n2,n3,n4)
print(f'você digitou os numeros {lista}')
print(f'temos {lista.count(9)} numeros 9 na lista')
cont = c = par = 0
while c < len(lista):
    if(lista[c] % 2 == 0):
        par += 1
    c += 1
while cont < len(lista):
    if lista[cont] == 3:
        print(f'a posição do numero 3 é {cont}')
    if(lista.count(3) != 1 and cont == len(lista) - 1):
        print('o valor 3 não apareceu')
    cont += 1
print(f'temos {par} numeros par')

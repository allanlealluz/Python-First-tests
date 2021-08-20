resp = ''
valor = []
pares = []
impar = []
while resp.upper() != 'N':
    n = int(input('digite um numero: '))
    valor.append(n)
    resp = input('Quer continuar? [S,N] ')
for c,v in enumerate(valor):
    if(valor[c] % 2 == 0):
        pares.append(valor[c])
    else:
        impar.append(valor[c])
print(valor)
print(f'os numeros pares são {pares}')
print(f'os numeros impares são {impar}')
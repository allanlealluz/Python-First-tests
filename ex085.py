c = 0
numeropar = []
numeroimpar = []
numeros = [[],[]]
while c < 8:
    n = int(input('Digite um numero: '))
    if(n % 2 == 0):
        numeros[0].append(n)
    else:
        numeros[1].append(n)
    c += 1
print(numeros)
print(numeros[0])
print(numeros[1])


n = int(input('digite um numero: '))
proximo = 0
anterior = 0
while proximo < n:
    print(proximo,end='')
    print('->' if proximo < n - anterior else '',end='')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo += 1
    

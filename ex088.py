import random,time
print('-='*5,end='')
print("Bem vindo ao palpilteiro",end='')
print('-='*5)
njogos = int(input('Quantos jogos? '))
numeros = []
conjunto = []
c = 0
t = 1
if(njogos > 0):
 while c < njogos:
    for rand in range(0,6):
     n = random.randint(1,60)
     if(n not in numeros ):
      conjunto.append(n)
    numeros.append(conjunto[:])
    conjunto.clear()

    while t < len(numeros)+1:

        print(f'Jogo {t}: {numeros[t-1]}')
        t+=1
    time.sleep(1)
    c+= 1

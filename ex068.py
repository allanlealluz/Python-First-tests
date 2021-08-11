import random
palpite = 'null'
c= 0
while True:
    numrand = random.randint(1,100)
    palpite = input('par ou impar? ')
    n = int(input('escolha um numero de 1 a 100'))
    result = numrand + n
    if result % 2 == 0 and palpite.upper() == 'PAR':
        print('você ganhou')
        c += 1
    elif result % 2 != 0 and palpite.upper() == 'IMPAR':
        print('você ganhou')
        c += 1
    else:
        print('você perdeu')
        break
print(f'você perdeu, porem ganhou {c} ',end='')
print('vezes' if c > 1 else 'vez')




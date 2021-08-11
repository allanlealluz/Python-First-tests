import random
randnum = random.randint(1,10)
r = 0
n = 0
while r != randnum:
    r = int(input('um numero de 1 a 10: '))
    n += 1
print('você acertou após {} tentivas'.format(n))
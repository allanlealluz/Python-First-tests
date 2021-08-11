print('Bem vindo a fabrica de fatoriais')
n1 = int(input('digite um numero: '))
f = 1
print('!{} = '.format(n1),end='')
while n1 != 0:
    print('{}'.format(n1), end='')
    print('x' if n1 > 1 else '=', end='')
    f *= n1
    n1 -= 1
print(f, end='')





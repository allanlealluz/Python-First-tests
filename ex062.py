inicial = int(input('inicio: '))
progessao = int(input('progressao de: '))
c = inicial
while c < 11:
    print("{}".format(c),end='')
    print('->' if c < 11 - progessao else '',end='')
    c += progessao
resp = input('\nQuer mostrar mais termos? S/N')
if resp.upper() == 'S':
 mais = int(input('quantos mais? '))
 while mais != 0:
    mais = int(input('quantos mais? '))
    c = inicial
    while c < mais:
        print("{}".format(c), end='')
        print('->' if c < mais - progessao else '', end='')
        c += progessao


          
inicial = int(input('inicio: '))
progessao = int(input('progressao de: '))
c = inicial
while c < 11:
    print("{}".format(c),end='')
    print('->' if c < 11 - progessao else '',end='')
    c += progessao


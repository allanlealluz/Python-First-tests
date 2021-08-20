valor = []
resp = ''
while resp.upper() != 'N':
    n = int(input('digite um numero'))
    if n in valor:
        print('valor duplicado não vou adicionar')
    else:
        print('valor adicionado com sucesso')
        valor.append(n)

    resp = input('Quer continuar? [S,N]')
print(sorted(valor))
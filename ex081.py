resp = ''
valor = []
while resp.upper() != 'N':
    n = int(input('digite um numero '))
    valor.append(n)
    resp = input('quer continuar? [S,N]')
    print(f'foram digitados {len(valor)} numeros')
    print(f'em ordem inversa {sorted(valor,reverse=True)}')
if(5 in valor):
    print('5 está na lista')
else:
    print('5 não está na lista')
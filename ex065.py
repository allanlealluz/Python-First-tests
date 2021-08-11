r = ''
result = 0
c = 0
while r.upper() != 'N':
    n = int(input('digite um numero: '))
    result += n
    r = input('Quer continuar? S/N ')
    c += 1
print(f'a média dos numeros digitados foi equivalente a {result / c} ')

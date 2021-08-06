numero = int(input('digite um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
print(u,d,c)
print('qual foi?' if numero <= 3 else 'suave')
print('yesy')
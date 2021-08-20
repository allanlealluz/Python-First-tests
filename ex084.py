pessoas = []
pessoa = []
c = 0
maior = menor = 0
while c < 5:
    pessoa.append(input('Qual é seu nome? '))
    pessoa.append(float(input('Qual é seu peso? ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if(pessoa[1] > maior):
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    c += 1

print(pessoas)
print(maior)
print(menor)
print('Os maiores pesos são ',end='')
for p in pessoas:
    if(p[1] == maior):
        print(f'{p[0]}',end='')
print('Os menores pesos são ',end='')
for p in pessoas:
    if(p[1] == menor):
        print(f'{p[0]}',end='')


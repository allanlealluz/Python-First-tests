valores = [1,3,5,6,9,8,7,71]
for v,c in enumerate(valores):
    print(f'Na posição {v} encontrei {c}')
lista = list()
for cont in range(0,5):
    lista.append(int(input('digite um valor: ')))
print(lista)
a = [1,2,3,5]
b = a[:] # b = a faz uma ligação entre os dois para resolver coloque [:]
b[2] = 6
print(a)
print(b)
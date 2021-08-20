teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
pessoas = [['jorge',19],['Ana',33],['Conda',69]]
print(pessoas[2][1])
for p in pessoas:
    print(p[0])
listagem = ('Pão',1,'Leitinho',1.99,'Frango',10.50)
c = 0
print('-------------------\nListagem de Preços\n-------------------')
while c < len(listagem):
    if(c == 0):
     print(f'{listagem[c]:.<20}R${listagem[c+1]}')
    elif(c == 2):
     print(f'{listagem[c]:.<20}R${listagem[c+1]}')
    elif (c == 4):
     print(f'{listagem[c]:.<20}R${listagem[c + 1]}')
    elif (c == 5):
     print(f'{listagem[c-1]:.<20}R${listagem[c]}')
    c += 1
resp = ''
precotot = 0
maiormil = 0
menor = cont = 0
nomemeno = ''
while resp.upper() != 'N':
    nomeprod = str(input('Nome do produto: '))
    precoprod = int(input('Preço do produto: '))
    precotot += precoprod
    cont += 1
    if(cont == 1):
        menor = precoprod
    else:
     if precoprod < menor:
        menor = precoprod
        nomemeno = nomeprod
    if(precoprod > 1000):
        maiormil += 1
    resp = input('Você vai comprar mais alguma coisa onii-chan? [S,N]')
print(precotot)
print(maiormil)
print(f'o produto mais barato foi {nomemeno} que custava R${menor:.2f}')

n1 = int(input('digite um numero: '))
n2 = int(input('digite um ultimo numero: '))
com = int(input('o que você quer fazer?\n digite 1 para somar \n digite 2 para multiplicar \n digite 3 para ver qual dos numeros é maior \n digite 4 para novos numeros \n e por fim digite 5 para sair'))
while com != 5:
    if(com == 1):
        print(n1 + n2)
    elif(com == 2):
        print(n1 * n2)
    elif(com == 3):
        if(n1 > n2):
            print('{} é maior'.format(n1))
        elif(n2 > n1):
            print('{} é maior'.format(n2))
        else:
            print('eles tem o mesmo tamanho')
    if(com == 4):
        n1 = int(input('digite um numero: '))
        n2 = int(input('digite um ultimo numero: '))

    com = int(input('e agora? '))
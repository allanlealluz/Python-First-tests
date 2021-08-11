numero = int(input('manda um numero ai '))
tipo = int(input('escolha um tipo de conversão de 1 a 3 '))
if(tipo == 1):
 print('\33[1;33m'+bin(numero))
elif(tipo == 2):
    print('\33[1;33m'+oct(numero))
elif(tipo == 3):
    print('\33[1;33m'+hex(numero))
else:
    print('tipo invalido')
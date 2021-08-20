numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorce','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('digite um numero: '))
while True:
    if(n > 0 and n <= 20):
        break
    n = int(input('tente denovo digite um numero: '))
print(f'o numero digitado em extenso fica {numeros[n]}')

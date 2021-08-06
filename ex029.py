vel = float(input('qual a velocidade? '))
if(vel > 80):
    tax = (vel - 80) * 7
    print('você ultrapassou a velocidade é tera uma multa de {} reais'.format(tax))
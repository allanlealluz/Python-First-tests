viagem = int(input('qual a distância da viagem? '))
if(viagem > 200):
    print('a viagem vai custar {} reais'.format(viagem * 0.45))
else:
    print('a viagem vai custar {} reais'.format(viagem * 0.50))
times = ('Atletico-MG', 'Palmeiras', 'Fortaleza EC', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Ceara', 'Santos',
         'Atletico Goianiense', 'Bahia', 'Internacional', 'Corinthians', 'Fluminense', 'Juventude', 'Sport',
         'São Paulo', 'America-MG', 'Cuiabá', 'Grêmio', 'Chapecoense')
print(f'os primeiros 5 times são {times[0:5]}')
print(f'os ultimos 4 times são {times[-5:-1]} ')
print(f'em ordem alfabetica {sorted(times)}')
for cont in range(0, len(times)):
    if times[cont] == 'Chapecoense':
        print(f'a posição da chapecoence é {cont}')



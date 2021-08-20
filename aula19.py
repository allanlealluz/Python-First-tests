filme = {
    'titulo' : 'StarWars',
     'ano' : 1977
}
filme['autor'] = 'George Lucas'
print(f'O Filme {filme["titulo"]} foi feito em {filme["ano"]}')
print(filme.keys())
print(filme.values())
print(filme.items())
for f,s in filme.items():
    print(f'{f} {s}')

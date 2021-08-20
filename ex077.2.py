vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viajar', 'Elegante', 'Animal', 'Carro', 'Brasileiro', 'Abacate')
for palavra in palavras:
    print(f'as vogais de {palavra} são ',end='')
    for letra in palavra:
        if(letra.lower() in vogais):
            print(f'{letra.lower()} ',end='')
    print('')
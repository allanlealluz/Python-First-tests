import random
from pygame import mixer

mixer.init()

print('Jogo da adivinhação (TESTE SUA SORTE) ')
print('O nosso programa irá pensar em um número de 0 a 5, tente adivinhar!! Boa sorte.')
n1 = (random.randint(0, 5))
n2 = int(input('E então.... Qual número você escolheu? '))

if n2 == n1:
    print('Parabens, você acertou!!!')
    mixer.music.load('plun.mp3')
    mixer.music.play()
    input()

else:
    print('Você errou :( mais sorte na próxima vez :)')
    mixer.music.load('plun.mp3')
    mixer.music.play()
    input()
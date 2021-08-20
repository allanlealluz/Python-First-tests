lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
lanche2 = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Oloco meu virei o faustão')


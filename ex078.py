c = 0
valores = []
while c < 5:
    valores.append(int(input('digite um numero')))
    c += 1
print(valores)
menor = valores[0]
maior = valores[0]
pos = []
pos2 = []
t = 0
for c,v in enumerate(valores):
    if(valores[c] <= menor):
       menor = valores[c]
       pos.append(c)

    if(valores[c] >= maior):
        maior = valores[c]
        pos2.append(c)
while t < len(pos2):
    if(pos2[-1] != pos2[t]):
        print(pos2[-1])
        print(pos2[t])
        pos2.remove(pos2[t])
    t+=1
while t < len(pos):
    if(pos[-1] < pos[t]):
        pos2.remove(pos[t])
    t+=1

print(f'o maior valor é {maior} na posição {pos2}')
print(f'o menor valor é {menor} na posição {pos}')

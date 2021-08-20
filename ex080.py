valor = []
c = 0
while c < 5:
   n = int(input('digite um numero '))
   if c == 0 or n > valor[-1]:
    valor.append(n)
   else:
    pos = 0
    while pos < len(valor):
        if(n <= valor[pos]-1):
            valor.insert(pos,n)
            break
        pos += 1
   print('-=-'*30)
   c += 1
print(valor)
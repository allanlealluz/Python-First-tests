expre = input('digite uma expressão aritmetica: ')
pilha = []
for v in expre:
    if v == '(':
        pilha.append('(')
    elif v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print(pilha)
if len(pilha) == 0:
    print('expressão valida')
else:
    print('Sua expressão está errada')

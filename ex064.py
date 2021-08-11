c = 0
result = 0
n = int(input('digite um numero'))
while n != 999:
 n = int(input('digite um numero'))
 if(n != 999):
  result += n
 c += 1
print('foram digitados {} numeros '.format(c))
print(result)

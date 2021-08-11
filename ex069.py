maioridade = 0
homens = 0
novinha = 0
while True:
    print('---------------------\nCadastre uma pessoa\n---------------------')
    idade = int(input('qual é a sua idade? '))
    sexo = input('Qual é seu sexo? [M,F] ')
    while sexo.upper() != 'M' and sexo.upper() != "F":
        sexo = input('Qual é seu sexo? [M,F] ')
    if(idade > 18):
        maioridade += 1
    if(sexo.upper() == 'M'):
        homens += 1
    if(sexo.upper() == 'F' and idade < 20):
        novinha += 1
    resp = input('Quer continuar? [S,N] ')
    if(resp.upper() == 'N'):
        break
print(f'temos {maioridade} pessoas maiores de idade ',end='')
print(f'temos {homens} homens cadastrados ',end='')
print(f'temos {novinha} novinhas cadastradas')

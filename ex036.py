print('bem vindos a All-Creditos, a melhor creditora da linguagem python')
valorCasa = float(input('qual o valor da casa? '))
salario = float(input('Salario: '))
anos = float(input('quantos anos vai ser o emprestimo? '))
prestacao = valorCasa / (12 * anos)
print(prestacao)
if(prestacao > salario * 0.30):
    print('o emprestimo não pode ser feito')
else:
    print('tudo correto')
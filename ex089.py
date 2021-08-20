resp = ''
alunos = []
aluno = []
nota = []
while resp.upper() != 'N':
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = nota1 + nota2 / 2
    nota.append(nota1)
    nota.append(nota2)
    aluno.append(nome)
    aluno.append(media)
    aluno.append(nota[:])
    nota.clear()
    alunos.append(aluno[:])
    aluno.clear()
    resp = input('Quer continuar? [S,N]')
for alu in alunos:
    print(f'Aluno:{"alu[0]":<10} ',end='')
    print(f'Nota Media:{alu[1]}')
perg = int(input('Quer ve a nota de quem? [digite em numeros, ao digitar 999 termina o programa]'))
while perg != 999:
    if(alunos[perg]):
     print(alunos[perg][0])
    perg = int(input('Quer ve a nota de quem? [digite em numeros, ao digitar 999 termina o programa]'))
print(alunos)
boletim=[]
aluno=[]
while True:
    boletim.append(str(input('Nome: ')).strip().capitalize())
    boletim.append(float(input('Nota 1: ')))
    boletim.append(float(input('Nota 2: ')))
    aluno.append(boletim[:])
    boletim.clear()
    resp=str(input('Continuar [S/N]: ').upper().strip())
    if resp not in 'SN':
        resp=str(input('ERRO! Continuar? [S/N]').upper().strip())
    if resp=='N':
        break
print('=-='*10)
print(f'{'No.':<4}|{'NOME':<10}|{'MEDIA':<10}|{'STATUS'}')
print('-'*30)
c=0
aluno.sort()
for p in aluno:
    media= (p[1]+p[2])/2
    print(f'{c:<4}{p[0]:<10}{media:<10.1f}',end=' ')
    if media <5:
        print('REPROVADO')
    elif media >=5 and media <6:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')
    c= c+1
print('=-='*20) 
while True:
    notaaluno=int(input('Deseja ver a nota de qual aluno ?(999 interrompe): '))
    if notaaluno == 999:
        break
    if notaaluno >=0:
        print(f'O aluno solicitado foi: {aluno[notaaluno]}')
print('ENCERRADO')
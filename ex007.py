print('-'*50)
print('Sistema de notas Escola Macaco Cansado')
aluno= str(input('Digite o nome completo do Aluno: '))
n1= float(input('Nota primeira avaliação: '))
n2= float(input('Nota segunda avaliação: '))
n3= float(input('Nota terceira avaliação: '))
m= (n1+n2+n3)/3
print('-'*50)
print('O aluno {:>20}\nTeve média {:>15.2f}'.format(aluno,m))
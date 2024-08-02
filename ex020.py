from random import shuffle
fs= str(input('Nome do primeiro aluno: '))
ss= str(input('Nome do segundo aluno: '))
ts= str(input('Nome do terceiro aluno: '))
qs= str(input('Nome do quarto aluno: '))
lista= [fs,ss,ts,qs]
shuffle(lista)
print('A ordem escolhida foi: {}'.format(lista))

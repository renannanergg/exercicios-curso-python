import random
'''pa= str(input('Nome do primeiro aluno: '))
sa= str(input('Nome do segundo aluno: '))
ta= str(input('Nome do terceiro aluno: '))
qa= str(input('Nome do quarto aluno: '))
print('O aluno escolhido foi: {} '.format(random.choice([pa,sa,ta,qa]))'''

import random
pa= str(input('Nome do primeiro aluno: '))
sa= str(input('Nome do segundo aluno: '))
ta= str(input('Nome do terceiro aluno: '))
qa= str(input('Nome do quarto aluno: '))
lista= [pa,sa,ta,qa]
escolhido= random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

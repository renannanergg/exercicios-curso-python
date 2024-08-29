import emoji
nome = input('Qual seu nome ?').strip().title()
# Criando Biblioteca de Cores
cor= {'limpa':'\033[m',
      'pretobranco':'\033[1;30;107m'}
print('Muito prazer em te conhecer, {}{}{}!'.format(cor['pretobranco'],nome,cor['limpa']))
print('Seja bem vindo(a)', emoji.emojize(':beaming_face_with_smiling_eyes:'))

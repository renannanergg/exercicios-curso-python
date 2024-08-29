#Importar biblioteca para data
from datetime import date

#Descorbir a idade do user
nasc= int(input('Ano de nascimento: '))
idade= (date.today().year - nasc)
print('O atleta tem \033[1;34m{}\033[m anos'.format(idade))
#Condicional para classificar o user
if idade <= 9:
    print('Sua classificação é \033[1;33mMIRIM\033[m')
elif idade <=14:
    print('Sua classificação é \033[1;32mINFANTIL\033[m')
elif idade <=19:
    print('Sua classificação é \033[1;34mJÚNIOR\033[m')
elif idade <=25:
    print('Sua classificação é \033[1;31mSÊNIOR\033[m')
else:
    print('Sua classificação é \033[7;97mMASTER\033[m')

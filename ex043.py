#Descobrir peso e altura do user para calcular o IMC
altura= float(input('Qual sua altura (M)?  '))
peso= float(input('Qual seu peso (KG) ? '))
imc= peso / (altura ** 2)
print('Seu IMC é \033[1;34m{:.1f}\033[m'.format(imc))
#Condicionais para classificar IMC
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
    
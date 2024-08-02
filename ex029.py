vel= float(input('Qual a velocidade do carro: ')) # descobrir a velocidade do carro
mult= (vel-80) * 7 # valor da multa se passar do limite de 80 (diferenca entre vel e o limite= execesso * valor por km)
if vel <= 80.00:
    print('Sua velocidade atual é de {}km e está dentro do limite permitido\n'.format(vel))
else:
    print('Voce foi MULTADO !!\nVoce estava a {}km e o limite é {}km\nMulta no valor de R$ {}'.format(vel,80,mult))
print('Dirija com cuidado e tenha um bom dia !')
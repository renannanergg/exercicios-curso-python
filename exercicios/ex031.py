distancia= float(input('Informe a distancia da viagem em km : '))    #descobrir a distancia
if distancia <= 200:   #se a distancia foi menor que 200km
    vlrp= distancia * 0.50
    print('Sua viagem de {}km ira custar R$ {}'.format(distancia,vlrp))
else:                 #se a distancia for maior que 200km
    vlrp= distancia * 0.45
    print('Sua viagem de {}km ira custar R$ {}'.format(distancia,vlrp))
print('Obrigado por viajar conosco !\nBoa Viagem !!')
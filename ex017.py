import math
catop= float(input('Digite o comprimento do cateto oposto: '))
catj= float(input('Digite o comprimento do cateto adjacente:'))
hi= math.hypot(catop,catj)
print('A hipotesuna tem o valor de {:.2}'.format(hi))

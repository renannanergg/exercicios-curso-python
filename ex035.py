print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
# Descobrir o tamanho dos triangulos
r1= float(input('Digite o primeiro segmento: '))
r2= float(input('Digite o segundo segmento: '))
r3= float(input('Digite o terceiro segmento:'))
# Condição para existencia de triangulo
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Triangulo PODERA ser formado')
else:
    print('Triangulo NÃO PODERA ser formado')
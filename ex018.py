import math
ang= float(input('Digite um angulo: '))
seno= math.sin(math.radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang,seno))
cos= math.cos(math.radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang,cos))
tang= math.tan(math.radians(ang))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ang,tang))

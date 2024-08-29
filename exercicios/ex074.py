import random
from random import randint
aleatorio=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
ordem=(sorted(aleatorio))
maior=ordem[4]
menor=ordem[0]
print(f'Os valores aleatórios foram: {aleatorio}')
print(f'Os valores em ordem {ordem}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
#print(f'O maior valor foi {max(aleatorio)}')
#print(f'O menor valor foi {min(aleatorio)}')

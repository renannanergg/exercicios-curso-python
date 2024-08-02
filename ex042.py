# Descobrir as medidas de a,b e c (medidas do triangulo)
a=float(input('Primeiro Segmento: '))
b=float(input('Segundo Segmento: '))
c=float(input('Terceiro Segmento: '))
# Condição para o triangulo existir:
if a < b + c and b < a + c and c < a + b:
    print('Pode a ser um triangulo ', end='')
    if a == b == c:
        print('\033[1;31mEquilatero\033[m')
    elif a != b != c != a:
        print('\033[1;33mEscaleno\033[m')
    else:
        print('\033[1;34mIsoceles\033[m')

else:
    print('Não pode ser um triangulo')

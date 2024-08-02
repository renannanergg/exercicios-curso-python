maisp=0
maisl=0
for pess in range(1,6):
    peso= float(input('Digite o peso da {}º pessoa: '.format(pess)))
    if pess==1:
        maisp = peso
        maisl = peso
    else:
        if peso > maisp:
            maisp=peso
        elif peso < maisl:
            maisl=peso
print('-=-'*20)
print('O \033[1;34mmaior\033[m peso registrado foi de \033[1;34m{}KG\033[m'.format(maisp))
print('O \033[1;31mmenor\033[m peso registrado foi de \033[1;31m{}KG\033[m'.format(maisl))

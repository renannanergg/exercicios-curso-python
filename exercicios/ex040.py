num1= float(input('Digite a primeira nota: '))
num2= float(input('Digite a segunda nota: '))
media= ( num1 + num2 )/2
if media >= 7:
    print('A média do aluno foi de \033[1;32m{:.2f}\033[m'.format(media))
    print ('O aluno foi \033[1;32mAPROVADO\033[m')
elif media < 7 and media > 5:
    print('A média do aluno foi de \033[1;33m{:.2f}\033[m'.format(media))
    print('O aluno esta de \033[1;33mRECUPERAÇÃO\033[m')
else:
    print('A média do aluno foi de \033[1;31m{}\033[m'.format(media))
    print('O aluno foi \033[1;31mREPROVADO\033[m')




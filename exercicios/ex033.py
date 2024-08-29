n1= int(input('Digite o primeiro valor: '))       #descobrir valor 1
n2= int(input('Digite o segundo valor: '))        #descobrir valor 2
n3= int(input('Digite o terceiro valor: '))       #descobrir valor 3
# descobrir quem é menor
menor= n1   #pressupor que n1 é o menor para poupar um if
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
# descobrir o maior valor
maior= n1   #pressupor que n1 é o maior para poupar um if
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

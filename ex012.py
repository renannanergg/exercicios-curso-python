prcsd= float(input('Digite o preço do produto em R$: '))
prccd= prcsd - (prcsd * 5 / 100)
print ('O produto sem desconto R$ {:.2f}\nCom desconto R$ {:.2f}'.format(prccd,prcsd))


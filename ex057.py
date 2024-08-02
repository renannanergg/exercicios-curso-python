r= str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while r not in 'MF':
    r=str(input('Dados invalidos,informe novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(r)) 
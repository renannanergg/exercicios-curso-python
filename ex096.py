def area(alt,larg):
    area=alt*larg
    print(f'A area de um terreno de {larg}x{alt} é de {area}m2')


print('=='*10)
print('   Analise de Área     ')    
print('=='*10)
larg= float(input('Largura(m): '))
alt=float(input('Altura(m): '))
area(alt,larg)
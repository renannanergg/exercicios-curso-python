from datetime import datetime
atual=(datetime.today().year)
registro=dict()
registro['nome']=str(input('Nome: ').title().strip())
nasc=int(input('Ano de Nascimento: '))
registro['idade']=atual-nasc
registro['ctps']=int(input('Carteira de Trabalho(0 não tem): '))
if registro['ctps']!=0:
    registro['contratação']=int(input('Ano de Contratação: '))
    registro['salário']=float(input('Salário (R$): '))    
print('-=-'*10)
print('-=-'*10)
print(f'--O nome é: {registro["nome"]}')
print(f'--A idade é: {registro["idade"]} anos')
if registro['ctps']==0:
    print('--Não há registro de CTPS')
else:
    print(f'--Contratado em: {registro["contratação"]}')
    print(f'--Salário: {registro["salário"]}')
    registro['aposentadoria']=registro['contratação']+30
    print(f'--Poderá se aposentar em: {registro["aposentadoria"]} com {registro["aposentadoria"]-nasc} anos')
print(registro)




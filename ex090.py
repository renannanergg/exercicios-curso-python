boletim={}
while True:
    print('=='*10)
    boletim['Nome']=str(input('Nome aluno: ').capitalize().strip())
    boletim['Média']=float(input(f'Média do {boletim["Nome"]}:'))
    print('=='*10)
    print(f'O nome do aluno é {boletim["Nome"]}')
    print(f'A média do {boletim["Nome"]} é {boletim["Média"]}')
    if boletim["Média"]<6:
        boletim['Status']='Reprovado'
    if boletim["Média"]>=6 and boletim["Média"]<7:
        boletim['Status']='Recuperação'
    if boletim["Média"]>7:
        boletim['Status']='Aprovado'
    print(f'Status: {boletim["Status"]}')
    print('=='*10)
    resp=str(input('Continuar [S/N]: ').upper().strip())
    if resp=='N':
        break
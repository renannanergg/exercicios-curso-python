def notas(*n,sit=False):
    """
    Calcular a média, verificar a maior e menor nota e a situação do aluno
    n: notas dos alunos, qualquer quantidade
    sit(opicional): mostrar a situação do aluno
    
    """
    resp=dict()
    maior=n[0]
    menor=n[0]
    média=totn=0
    for num in n:
        totn= totn+ num
        if num > n[0]:
            maior=num
        if num < n[0]:
            menor=num
    média= totn / (len(n))
    resp['Media']=média
    resp['Total de notas']=len(n)
    resp['Maior nota']=maior
    resp['Menor nota']=menor
    if sit==True:
        if média >=7:
                resp['situação']='ÓTIMA'
        if  média >= 5 and média <7:
                resp['situação']='BOA'
        if média <5:
                resp['situação']='RUIM'
    print(resp)
        


#Pricipal
notas(8,5,9)
help(notas)

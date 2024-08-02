def maior(*num):
    tot=len(num)
    cont=0
    maior=0
    while cont != tot:
        if len(num)==1:
            maior=num[0]
        elif num[cont]> maior:
            maior=num[cont]
        cont=cont+1
           
    print('=='*20)
    print(f'Analisando os valores {num}, temos: ')
    print(f'Foram analisados {tot} valores')
    print(f'O maior valor foi {maior}')
    print('=='*20)


#Principal
maior(2,5,8,4)
maior(5,10,20)
maior(5,6,2,18,35,44,58,12,99,3,25)
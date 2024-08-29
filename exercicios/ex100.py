from random import randint
num=[]
def sorteia(lista):
    for n in range(0,5):
        lista.append(randint(0,10))
    print(f'Foram sorteados os numeros {lista}')

def somapar(lista):
    totpar=0
    for n in num:
        if n %2==0:
            totpar= totpar + n
    print(f'Somando os valores pares de {num} temos o total de {totpar}')


#Principal
sorteia(num)
somapar(num)
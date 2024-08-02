totais=[[],[]]
for c in range(1,8):
    n=(int(input(f'Digite o {c}º valor: ')))
    if n % 2 ==0:
        totais[0].append(n)
    if n % 2 ==1:
        totais[1].append(n)
totais[0].sort()
totais[1].sort()
print('=-='*20)
print(f'Os numeros pares são {totais[0]}')
print(f'Os numeros impares são {totais[1]}')

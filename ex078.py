valores=[]
for v in range(1,6):
    valores.append(int(input(f'Digite um numero na posição {len(valores)}: ')))
print(f'Os valores digitados foram: {valores}')
print(f'Em ordem numerica {sorted(valores)}')
for v in valores:
    if v == valores[0]:
        maior = valores[0]
        menor= valores[0]
    else:
        if v > maior:
            maior=v
        if v < menor:
            menor=v
print(f'O maior valor foi {maior} na posição {valores.index(maior)}')
print(f'O menor valor foi {menor} na posição {valores.index(menor)}')
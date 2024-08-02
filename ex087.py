matriz = [[0,0,0],[0,0,0],[0,0,0]]
totpar=stc=mai=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite o valor da posição [{l},{c}]:'))
print('=0='*15)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] %2==0:
            totpar= totpar + matriz[l][c]
        
    print()
for l in range(0,3):
    stc= stc + matriz[l][2]
for c in range(0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c]>mai:
        mai=matriz[1][c]
print('=0='*15)
print(f'A soma da terceira coluna é {stc}')
print(f'A soma dos pares é {totpar}')
print(f'O maior valor da segunda linha é {mai}')
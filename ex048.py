# Adicionar somador para somar os numeros multiplos de 3
s= 0
tot= 0
for c in range(0,501,3):    #Pular de 3 em 3 (multiplos de 3)
    if c % 2 == 1:          # Mostrar numeros impares
        s= s + 1
        tot= tot + c

print("A soma dos \033[1;33m{}\033[m números selecionados é \033[1;34m{}\033[m".format(s,tot))

'''s=0
tot=0
for c in range(1,501,2)     # Pular em numeros impares 
    if c % 3 == 0:          # Mostrar multiplos de 3
        s= s + 1
        tot= tot + c
print("A soma dos {} numeros selecionados é {} ".format(s,tot))'''
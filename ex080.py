valores= []
for c in range(1,6):
    v=(int(input('Digite um numero: ')))
    if c == 1:
        valores.append(v)
    elif v > valores[-1]:
        valores.append(v)
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos,v)
                break
            pos = pos + 1
print(valores)
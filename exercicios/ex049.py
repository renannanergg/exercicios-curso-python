n= int(input('Digite um numero: '))
tot= 0
print("-=-"*15)
for i in range(1,11):
    tot= i * n
    print("\033[1;32m{}\033[m x \033[1;33m{}\033[m= \033[1;34m{}\033[m".format(n,i,tot))
print("-=-"*15)

extenso= ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze'
          ,'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
resp='S'
while resp =='S':
    print('=='*20)
    numero= int(input('Digite um numero de 0 a 20: '))
    print(f'O numero digitado foi {extenso[numero]}')
    resp= str(input('Continuar ? [S/N] ')).strip().upper()
    if numero <0 and numero >20:
        break
print('FIM')
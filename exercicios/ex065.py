r=' '
totn=0
somv=0
mav=0
mnv=0
while r != 'N':
    n=int(input('Digite um valor: '))
    totn= totn + 1
    somv= somv + n
    if totn==1:
        mav= n
        mnv= n
    else:
        if n > mav:
            mav=n
        if n < mnv:
            mnv=n
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()
media= somv / totn
print('FIM')
print('Voce digitou {} numeros, totalizando {} e media {}'.format(totn,somv,media))
print('O maior numero digitado foi {}, e o menor foi {}'.format(mav,mnv))



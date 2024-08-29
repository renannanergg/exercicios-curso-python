# Descobrir o preço da compra
print('-=-'*30)
print('LOJAS RENUNCIAS')
print('-=-'*30)
preco= float(input('DIGITE O TOTAL DAS COMPRAS: R$'))
print('-=-'*30)
print('ESCOLHA A FORMA DE PAGAMENTO: ')
print('[1] A VISTA DINHEIRO/CHEQUE\n[2] A VISTA NO CARTAO\n[3] 2X NO CARTAO\n[4] 3X OU MAIS')
opcao= int(input('OPCAO: '))
if opcao == 1:
    precofinal = preco - (preco * 10/100)
    print('O total de R${:.2f} com desconto vai custar R${:.2f}'.format(preco,precofinal))
elif opcao == 2:
    precofinal = preco - (preco * 5/100)
    print('O total de R${:.2f} com desconto vai custar R${:.2f}'.format(preco,precofinal))
elif opcao ==3:
    precofinal = preco
    parcela= precofinal/ 2
    print('O total de R${:.2f} nao terá desconto e será divido em 2x'.format(preco))
    print('As parcelas serão de R${:.2f}'.format(parcela))
elif opcao ==4:
    precofinal = preco + (preco * 20/100)
    totparc= int(input('QUANTAS PARCELAS: '))
    parcela= precofinal / totparc
    print('O valor das parcelas serão de R${:.2f}'.format(parcela))
    print('O total de R${:.2f} com juros irá custar R${:.2f}'.format(preco,precofinal))
else:
    print('OPÇÃO INVÁLIDA')
print('-=-'*30)
print('OBRIGADO E VOLTE SEMPRE ! ')
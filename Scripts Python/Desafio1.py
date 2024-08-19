produto = 2000
imposto = 1500
iphone = produto+imposto
print('O preço do iPhone é de: R$'+ f"{iphone:.2f}")
print('Podendo ser parcelado em até 10x sem juros R$'+ f'{iphone/10:.2f}')

if iphone > 4000.00:
    print('O valor está Caro')
else:
    print('O valor Compensa')
    
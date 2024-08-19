#Faça um algoritmo que leia o preço de produto e mostre seu novo preço, com 5% de desconto

pd = float(input('Digite o valor do produto que queira o desconto de 5%: R$'))

off = pd - pd * (5/100)

print('-'*40)
print('\nValor do produto com o desconto: R${:.2f}\n\n'.format(off))

#Correção do Exercício: Correto
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere = US$1,00 = R$ 5,46

rs = float(input("Digite quando de dinheiro disponivel você tem: R$"))

dl = rs / 5.46

print('-'*40)
print('\nDoláres disponiveis: US${:.2f}\n'.format(dl))
print('-'*40)


#Correção do Exercício: Correto
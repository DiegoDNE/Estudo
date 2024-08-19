#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

al = int(input('Quantos dias o carro foi algudado?: '))
km = float(input('Quantos Km rodados nesse período?: '))

print('-'*40)
print('\nO Total a pagar é de: R${:.2f}'.format((al * 60 ) + (km * 0.15)))

#Correção do Exercício: Correto
#Faça um algoritmo que leia um salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite o seu salário para simular o aumento de 15%: R$'))

aum = sal + sal * (15/100)

print('-'*40)
print('\nO seu salário passaria para: R${:.2f}\n\n'.format(aum))

#Correção do Exercício: Correto
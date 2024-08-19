#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.  

"""ex: 
    Digete um número: 1834
    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1"""

n1 = int(input('Digite um número inteiro de 0 a 9999: '))

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('\n'+'-'*45)
print('\nUnidade:',u)
print('Dezenas:',d)
print('Centenas:',c)
print('Unidade de Milhar:',m)
print('\n'+'-'*45)
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: 
#Digite um número:6.127
#O número 6.127 tem a parte interia 6.

from math import trunc

n1 = float(input('Digite um número real: '))

print('-'*40)
print('\nO número escolhido foi {};\n'.format(n1))
print('A porção interira desse número é: {}\n\n'.format(trunc(n1)))
print('-'*40)

"""print('-'*45)
print('\nO número escolhido foi {};\n'.format(n1))
print('A porção inteira desse número é: {}\n\n'.format(int(n1)))
print('-'*45)"""


"""Caso use só 'Import math'. Na hora do .format, tem que ser usado 'math.*****', sendo os **** a função da biblioteca de matemática que deseja ser usado"""
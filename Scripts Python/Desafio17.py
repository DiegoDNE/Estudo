#Faça um programa que leia o comprimento de cateto oposto a do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

a = float(input('Digite o eixo Y:'))
b = float(input('Digite o eixo X:'))

#h = ((a ** 2)+ (b ** 2)) ** (1/2)
#h = sqrt(a * a + b * b)
h = hypot(a, b)

print('-'*45)
print('\nA Hipotenusa de um Triângulo retângulo com os eixos \nY = {} e X = {} \nÉ de: {:.2f}\n'.format(a, b, h))
print('-'*45)

"""Caso use só 'Import math'. Na hora do .format, tem que ser usado 'math.*****', sendo os **** a função da biblioteca de matemática que deseja ser usado"""

#Exercício Correto
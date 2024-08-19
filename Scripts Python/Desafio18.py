#Faça um programa que leia um ângulo qualquer a mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo.

"""import math

ang = float(input('Digite um ângulo: '))

print('-'*45)
print('\nÂngulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))
print('-'*45)"""


print('-'*45)
from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

print('-'*45)
print('\nÂngulo: {}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n\n'.format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
print('-'*45)

#Exercício Correto
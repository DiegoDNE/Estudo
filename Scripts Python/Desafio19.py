#Um professor que sortear um dos seus alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
n5 = input('Nome do quinto aluno: ')

nomes = [n1, n2, n3, n4, n5] #Isso é um lista

print('-'*50)
print('\nO Aluno escolhido foi: {}\n'.format(choice(nomes)))
print('-'*50)

#No Python, Listas ficam entre []

#Exercício Correto
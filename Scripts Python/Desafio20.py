#O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalho dos alunos.
#Faça um programa que leia o nome do alunos e mostre a ordem sorteada.

from random import shuffle

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
n5 = str(input('Digite o quinto nome: '))

nomes = [n1, n2, n3, n4, n5]
shuffle(nomes)

print('-'*50)
print('\nA ordem de apresentação é:\n{}'.format(nomes))
print('-'*50)

#Exercício Correto
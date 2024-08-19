#Faça um programa que leia uma frase pelo teclado e mostre: (input)

#>>> Quantas vezes aparece a letra A

#>>> Em que posição ela aparece pela primeira vez (Letra A)

#>>> Em que posição ela aparece pela última vez (Letra A)


frase = input('Digite uma Frase: ')

contagem = frase.count('a')
primeiro_a = frase.find ('a')
ultimo_a = frase.rfind('a')
print('\n'+'-'*45)
print('\nQuantas vezes aparece a letra A: {}'.format(contagem))
print('\nEm que posição aparece o primeiro A: {}'.format(primeiro_a))
print('\nEm que posição aparece o último A: {}'.format(ultimo_a))
print('\n'+'-'*45)







"""Não se pode aprender nada de uma lição que não seja acompanhada por dor, já que não se pode conseguir nada sem um sacrifício.
 Mas quando você aguenta essa dor e a supera, as pessoas conseguem um coração forte que não perde para nada. Sim, um coração de aço."""
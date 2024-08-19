#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

nome = input('Digite o nome completo: ')

silva = 'silva' in nome.lower()

print('\n'+'-'*45)
print('\nEsse nome tem "Silva": {} '.format(silva))
print('\n'+'-'*45)
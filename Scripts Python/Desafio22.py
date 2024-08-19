#Crie um programa que leia o nome completo de uma pessoa e mostre: (input)

#>>> O nome com todas as letras maiúsculas

#>>> O nome com todas as letras minúsculas

#>>> Quantas letras ao todo (sem considerar espaços)

#>>> Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')

print('-'*45,'\n')
print('Nome Completo: {}\n'.format(nome))
print('Em maiúsculo:', nome.upper())
print('\nEm minúsculo:', nome.lower())
print('\nQuantas letras tem ao todo:', len(nome.replace(' ', '')))
print('\nQuantas letras tem o primeiro nome:', len(nome.split()[0]))
print('\n'+'-'*45,)


#Correção Correta
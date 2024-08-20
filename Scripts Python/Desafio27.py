#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

#EX: Ana Maria de Souza

#primeiro = Ana
#último = Souza

nome = input('Digite o nome completo: ')

primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print('\n'+'-'*45)
print('\nO primeiro nome é: {}'.format(primeiro_nome))
print('\nO último nome é: {}'.format(ultimo_nome))
print('\n'+'-'*45)

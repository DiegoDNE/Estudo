#Um programa que recebe um número, mostre o número anterior e sucessor do número escolhido

n1 = int(input('Digite um número:'))

a = n1 - 1
s = n1 + 1
print('-'*20)
print('\nO número anterior ao escolhido é o número {}'.format(a))
print('\nO número sucessor ao escolhido é o número {}\n'.format(s))
print('-'*20)


#pode ser escrito da seguinte maneira também 

#Exclui os objetos "A e S" e no print coloque direto:
#print('O numero antecessor é:{}'.format(n1 - 1))
#print('O numero sucessor é:{}'.format(n1 +1))

#fazendo a soma direto no format

#Correção do Exercício: Correto
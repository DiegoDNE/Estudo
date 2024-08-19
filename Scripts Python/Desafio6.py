#Um programa que recebe um número, mostre seu dobro, seu triplo e sua Raiz Quadrada

n1 = int(input('Digite um número:'))

d = n1 * 2
t = n1 * 3
rq =  n1 ** (1/2)

print('-'*20)
print('\nO Dobro do número escolhido é {}.\nO Triplo do número escolhido é {}.\nA Raiz Quadrada do número escolhido é {:.1f}.\n'.format(d,t,rq))
print('-'*20)


#Correção do Exercício: Correto
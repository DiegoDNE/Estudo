#desenvolva um programa que leia as Três notas de um aluno, calcule e mostre sua média.

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))
m = (n1+n2+n3)/2

print('-'*20)
print('\nA média do aluno é de {:.1f}.\n'.format(m))
print('-'*20)

if m > float(6.0):
    print('\nAPROVADO\n')
else:
    print('\nREPROVADO\n')
print('-'*20)


#Correção do Exercício: Correto
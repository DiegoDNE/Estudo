n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

a = n1 + n2
s = n1 - n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
pt = n1 ** n2
print('-'*20)
print('N1 = {} e N2 = {}'.format(n1, n2))
print('-'*20)
print('\nA soma dos números é {}.\n\nA subitração dos números é {}.\n\nA multiplicação dos números é {}.\n\nA divisão dos números é {:.2f}.\n'.format(a,s,m,d))
print('A divisão inteira dos números é {}.\n\nA potência dos números é {}.\n\n'.format(di,pt))
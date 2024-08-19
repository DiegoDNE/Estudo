#Escreva um programa que leia um valor em metros e exiba convertido em CM e MM

m = float(input('Digite os metros:'))

cm = m * 100
mm = m * 1000

print('-'*20)
print('\nA medida em Metro para Centimetros é de {:.0f}cm e a medida em Milímetros é de {:.0f}mm\n'.format(cm, mm))
print('-'*20)


#Correção do Exercício: Correto
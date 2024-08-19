#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a # quantidade de tinta necessária para pinta-la. 
#Sabendo que cada litro de tinta pinta um área de 2m².

y = float(input('Digite quando Metros de Altura tem a parede(em metros): '))
x = float(input('Digite quando Metros de Largura tem a parede(em metros): '))

m2 = y * x
lt = m2 / 2
print('-'*40)
print('\nA parede tem o total de {}m²\n'.format(m2))
print('-'*40)
print('Seriam necessários, {:.1f} latas de tinta.\n\n'.format(lt))

#Correção do Exercício: Correto
#Faça um programa que converta a temperatura de C° para F°

temp = float(input('Informe a temperatuda em C°: '))

print('-'*40)
print('\nA temperatura de {}C° corresponde a {:.1f}F°\n'.format(temp, temp * 9 / 5 + 32))
print('-'*40)

#Correção do Exercício: Correto
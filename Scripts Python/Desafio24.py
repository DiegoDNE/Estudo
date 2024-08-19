#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo" ou São

cidade = str(input('Digite o nome da sua Cidade: ')).strip()

#Pra saber se começa com Santo ou São, fica assim:
santo_ou_sao = cidade.lower().startswith('santo') or cidade.lower().startswith('são')

#Pra saber se tem Santo ou São no nome, fica assim: 
#santo_ou_sao = 'Santo' in cidade.lower() or 'São' in cidade.lower()


#o 'OR' combina as duas condições; se qualquer uma delas for verdadeira será True.
#utiliza-se o Lower pra garantir que erro de digitação (Minúsculas e maiúsculas) humana não interfira no resultado.

print('\n'+'-'*45)
#print('\nEssa cidade começa com Santo/São no nome: {} '.format(santo_ou_sao))
print('\nEssa cidade começa com Santo/São no nome: {} '.format(cidade.lower().startswith('santo') or cidade.lower().startswith('são')))
print('\n'+'-'*45)


#maneira do professor

teste2 = cidade[:5].lower() == 'santo' or cidade[:3].lower() == 'são'
print('teste:{}'.format(teste2))
#[0:5] ou [:5] = começando da letra 0 até a ultima letra de santo (que é  5)
# == -> os 2 iguais significa "é igual a..."
#só funcionaria pra saber uma unica palavra, que no caso é Santo
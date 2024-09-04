########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################

notas = [6.3, 7.5, 9.2, 5.1, 6.8]

soma = sum(notas)
media = soma/len(notas)

print(f'\nMédia - {media:.2f}\n')

#MAIORES
notas_maior_que_6 = list(filter(lambda x:x >=6, notas))
print(f'Notas maiores que 6 - {notas_maior_que_6}')

#MANORES
notas_menor_que_6 = list(filter(lambda x:x < 6, notas))
print(f'Notas menores que 6 - {notas_menor_que_6}')

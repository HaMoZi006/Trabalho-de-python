########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################

def calculo():
    numero = int(input("\nDigite um número: "))
   
    if (numero % 2 == 1):
        print(f"{numero} - ímpar")
    else:
        print(f"{numero} - par")
    reiniciar()

def reiniciar():
    escolha = input("Deseja digitar novamente? (s/n): ").lower()
    
    if(escolha == 's'):
        print("------------------------------------")
        calculo()
    elif (escolha == 'n'):
        exit(0)
    else:
        print("Caracter inválido")
        reiniciar()

calculo()#precisa para chamar a função. As funções são definidas antes e depois chamados, por isso aparece no fim

########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################

import random

def main():
    pontos_maq = 0
    pontos_jog = 0

    while True:
        print("1-Pedra")
        print("2-Papel")
        print("3-Tesoura")
       
        while pontos_jog <= 2 and pontos_maq <= 2:
            maquina = random.randint(1, 3)  # Gera um número aleatório entre 1 e 3

            try:
                numero = int(input("\nDigite um número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
                continue

            if numero > 3 or numero < 1:
                print("Número inválido. Tente novamente.")
                continue

            if maquina == 1 and numero == 3:  # Pedra vs Tesoura
                print("\nJogador - Tesoura")
                print("Máquina - Pedra")
                print("\nPedra ganha de Tesoura, você perdeu!")
                print("Vitória da máquina")
                pontos_maq += 1

            elif maquina == 3 and numero == 1:  # Tesoura vs Pedra
                print("\nJogador - Pedra")
                print("Máquina - Tesoura")
                print("\nPedra ganha de Tesoura, você venceu!")
                print("Vitória do jogador")
                pontos_jog += 1

            elif maquina == 1 and numero == 2:  # Pedra vs Papel
                print("\nJogador - Papel")
                print("Máquina - Pedra")
                print("\nPapel ganha de Pedra, você ganhou!")
                print("Vitória do jogador")
                pontos_jog += 1

            elif maquina == 2 and numero == 1:  # Papel vs Pedra
                print("\nJogador - Pedra")
                print("Máquina - Papel")
                print("\nPapel ganha de Pedra, você perdeu!")
                print("Vitória da máquina")
                pontos_maq += 1

            elif maquina == 2 and numero == 3:  # Papel vs Tesoura
                print("\nJogador - Tesoura")
                print("Máquina - Papel")
                print("\nTesoura ganha do Papel, você venceu!")
                print("Vitória do jogador")
                pontos_jog += 1

            elif maquina == 3 and numero == 2:  # Tesoura vs Papel
                print("\nJogador - Papel")
                print("Máquina - Tesoura")
                print("\nTesoura ganha do Papel, você perdeu!")
                print("Vitória da máquina")
                pontos_maq += 1

            else:
                print(f"Escolha da máquina: {maquina}")
                print("\nEmpate")

            print("\n-------------------------------------")

        print("\nRESULTADOS:")
        print(f"Pontos da máquina: {pontos_maq}")
        print(f"Pontos do jogador: {pontos_jog}")

        if pontos_maq == 3 and pontos_jog < 3:
            print("\nA máquina venceu!")
        
        elif pontos_jog == 3 and pontos_maq < 3:
            print("\nO jogador venceu!")

        print("\n-------------------------------------")
       
        jogar_novamente = input("Jogar novamente? (s/n): ")

        if jogar_novamente == 's':
            pontos_maq = 0
            pontos_jog = 0

        else:
            break
        
if __name__ == "__main__":
    main()

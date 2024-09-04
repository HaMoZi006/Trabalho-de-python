########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################

biblioteca = []

def adicionar_livro(titulo, autor, posicao=None):
    if posicao is None or posicao >= len(biblioteca) // 2:
        # Adiciona no final se a posição for None ou maior que o tamanho da lista
        biblioteca.append(titulo)
        biblioteca.append(autor)
    else:
        # Insere na posição específica
        biblioteca.insert(posicao * 2, titulo)#definir a posição. se 3 tres livros 3 posiçoes (3 autores)
        biblioteca.insert(posicao * 2 + 1, autor)#autor

def find (titulo):
    try:
        index = biblioteca.index(titulo)
        autor = biblioteca[index + 1]  # O autor está logo após o título na lista
        posicao = index // 2  # Calcula a posição do livro
        print(f"\n'{titulo}' - {autor} - Presente na biblioteca na posição {posicao + 1}")

    except ValueError:
        print(f"\nO livro '{titulo}' não foi encontrado na biblioteca.")

while (True):
    print("\n1- inserir \n2-Encontrar livro \n3-Mostrar lista")
    escolha = int(input("Escolha uma das opções: "))
    
    if(escolha == 1):#INSERIR
        titulo = input("\nDigite o livro: ")
        autor = input("Digite o autor: ")

        posicao = (input("Digite a posição onde deseja adicionar o livro (ou pressione Enter para adicionar ao final): "))

        if posicao.isdigit():
            posicao = int(posicao)

        else:
            posicao = None

        adicionar_livro(titulo, autor, posicao)

        print("\nLista atual de livros na biblioteca:")
        
        for i in range(0, len(biblioteca), 2):
            print(f'Título: {biblioteca[i]}, Autor: {biblioteca[i + 1]}')

    elif (escolha == 2):
        encontrar = input("Digite o título a ser encontrado: ")
       
        find(encontrar)

    elif (escolha == 3):
        print("\nLista completa de livros da biblioteca: \n")
        
        for i in range(0, len(biblioteca), 2):
            print(f'Título: {biblioteca[i]}, Autor: {biblioteca[i + 1]}')        
    else:
        print("insira um número válido")
        continue

    continuar = input("\nDeseja continuar alterando?: (s/n)").lower()
    if continuar != 's':
        print("\nPrograma encerrado.")
        break
    
#-------------------------------------------------------------------------------
#                           TESTE nº 1
#
# Curso: Fundamentos de Python
# UFCD/Módulo/Temática: UFCD: 10793 - Fundamentos de Python
# Ação: 10793_02/L
#
# Grupo 2
# Nome dos Formandos:   Andreia Martins
#                       Pedro Fragoso
#                       Ulisses Alvarinho
#
# Programa: Jogo da Forca
#-------------------------------------------------------------------------------

#inicio do programa


# Importação do módulo random para escolher uma palavra aleatória
import random

# Lista de palavras para o jogo da Forca
palavras = ["Ajuda", "Beato", "Areeiro", "Benfica", "Alvalade", "Marvila", "Campolide", "Lumiar", "Olivais"]

# Escolha aleatória de uma palavra da lista palavras[] e guarda na variavel palavra_secreta
palavra_secreta = random.choice(palavras).lower()


# Inicialização da lista de letras adivinhadas com o valor de "_" tendo em conta o tamanho da palavra_secreta
letras_adivinhadas = ["_"] * len(palavra_secreta)

# Número máximo de tentativas do jogador
max_tentativas = 5



#inicializa a lista alfabeto[] com os caracteres aceites pelo jogo. Dado que são nomes de cidades exclui tudo o que são numeros.     
alfabeto=[]
for i in range(65,91):  #adiciona as letras maiusculas do alfabeto segundo tabela ascii
    char = chr(65)
    alfabeto.append(char)
for i in range(97,123): #adiciona as letras minusculas do alfabeto segundo tabela ascii
    char = chr(i)
    alfabeto.append(char)
for i in range(192,256):  #adiciona as letras com acentuação/caracteres especiais do alfabeto segundo tabela ascii  
    char = chr(i)
    alfabeto.append(char)
    


# Função para desenhar o boneco da forca
def desenhar_boneco(tentativas):
    if tentativas == 0:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |    ")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   | ")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               | ")
        print("   |                                          |              |     |              |")
        print("   |                                                         |     |")
        print("   |                                                           ")
        print("   |                                                          ")
        print("   |                                                           ")
        print("___|___")
    elif tentativas == 1:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("___|___")
    elif tentativas == 2:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____                        |")
        print("   |                                          |      |    |                       |")
        print("   |                                          |      |    |                       |")
        print("   |                                          |      |____|                       |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("___|___")
    elif tentativas == 3:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____             ____       |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |____|           |____|      |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |          ____      ____      ____      ____")
        print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                                                                                |")   
        print("___|___")
    elif tentativas == 4:
       print("    ____________________________________________________________")
       print("   |/                                                           |")
       print("   |                                            |               |               |")
       print("   |                                           ( )             _|_             ( )")
       print("   |                                          |   |     ___   |   |   ___     |   |")
       print("   |                                          |   |____|   |__|   |__|   |____|   |")
       print("   |                                          |                                   |")
       print("   |                                          |               _____               |")
       print("   |                                          |              |     |              |")
       print("   |                                          |              |     |              |")           
       print("   |                                          |              |_____|              |")
       print("   |                                          |                                   |")
       print("   |                                          |       ____             ____       |")
       print("   |                                          |      |    |           |    |      |")
       print("   |                                          |      |    |           |    |      |")
       print("   |                                          |      |____|           |____|      |")
       print("   |                                          |                                   |")
       print("   |                                          |                                   |")
       print("   |                                          |                                   |          ____      ____      ____      ____")
       print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
       print("   |                                          |                                                                                |")
       print("   |                                          |                ____                                                            |")
       print("   |")
       print("___|___")
    else:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____             ____       |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |____|           |____|      |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |          ____      ____      ____      ____")
        print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                ____                                                            |")
        print("   |                                          |               |    |                                                          /")
        print("   |                                          |               |    |                                                         /")   
        print("   |                                          |               |    |                                                        |")
        print("   |..........................................|               |    |                                                        |.................")
        print("___|___")

# Função principal do jogo
def jogo_forca():
    tentativas = 0
    letras_erradas = []
    #letras_adivinhadas = palavra_secreta[] #Acrescentei dicionário letras corretas

    print("Olá, bem-vindo ao jogo da Forca!")          
    print("Adivinha a palavra secreta.")
    print("Vamos dar-te uma dica, é uma das freguesias de Lisboa!")


    while tentativas < max_tentativas:
        countprint=0    #contador para nr de impressoes no caso de vitoria
        letra = input("Digita uma letra: ").lower() #solicita uma letra ao jogador e converte para minuscula

        if letra in alfabeto and len(letra) == 1: #verifica se o caractere existe na lista albeto[] e se é um unico caratere
            if letra in letras_adivinhadas or letra in letras_erradas: #Impedir a repetição de letras.
                print("Já digistaste essa letra, tenta outra!")
                continue
            
            if letra in palavra_secreta:            # Verifica se a letra fornecida está presente na palavra secreta
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i] == letra:
                        if i==0:  #Assume/coloca o primeira letra sempre como maiscula
                            letras_adivinhadas[i] = letra.upper()
                        else:
                            letras_adivinhadas[i] = letra #restantes letras como minusculas
                        if countprint<1: #se contador menor 1 imprime mensagem de vitória
                            print("Parabéns, acertaste numa letra!") #acrescentei Parabéns acertaste, na letra.
                            countprint+=1
                        else:           
                            continue
            else:
                letras_erradas.append(letra)        #adiciona a letra errada à lista letras_erradas[]
                tentativas += 1                     #incrementa o numero de tentativas já usadas
                desenhar_boneco(tentativas)         #Exibe o boneco de acordo com o nº de tentativas
                   
            # Atualizar a exibição da palavra com a letra revelada, se estiver correta
            print("Palavra: ", " ".join(letras_adivinhadas))

            # Verificar se o jogador venceu ou perdeu o jogo
            if "_" not in letras_adivinhadas:
                print("Parabéns!! Ganhaste \o/ \o/")
                return
        elif len(letra) == 1:                       #faz o print de erro se for um único caractere mas que não está na lista alfabeto[], ou seja, numeros
            print("Inválido. Apenas letras. Tenta novamente.")
        else:                                       #faz o print de erro se nenhuma das opções
            print("Inválido. Digita uma única letra por favor.")

        print("Letras erradas: ", ", ".join(letras_erradas))

    print("Oh, não conseguiste! A palavra secreta era:", palavra_secreta,".Tenta outra vez!")

# Iniciar o jogo da forca
jogo_forca()
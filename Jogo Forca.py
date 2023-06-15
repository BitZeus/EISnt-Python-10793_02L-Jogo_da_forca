
# Importe o módulo random para escolher uma palavra aleatória
import random

# Lista de palavras para o jogo da Forca
palavras = ["ajuda", "beato", "areeiro", "benfica", "alvalade", "marvila", "campolide", "lumiar", "olivais"]

# Escolha uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# Inicialize a lista de letras adivinhadas
letras_adivinhadas = ["_"] * len(palavra_secreta)

# Número máximo de tentativas do jogador
max_tentativas = 5

alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print(alfabeto)

    


# Função para desenhar o boneco da forca
def desenhar_boneco(tentativas):
    if tentativas == 0:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |    ")
        print("   |                                           ( )             _|_             ( )")
       
        print("___|___")
    elif tentativas == 1:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
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
      
        print("___|___")
    elif tentativas == 3:
        print("    ___                                      |              |_____|              |")
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
        print("___|___")

# Função principal do jogo
def jogo_forca():
    tentativas = 0
    letras_erradas = []
   
    print("Olá, bem-vindo ao jogo da Forca!")
    print("Adivinha a palavra secreta.")
    print("Vamos dar-te uma dica, é uma das freguesias de Lisboa!")

    # Exibir os espaços em branco para cada letra da palavra
    print("Palavra: ", " ".join(letras_adivinhadas))

    while tentativas < max_tentativas:
        countprint=0    #contador para nr de impressoes no caso de vitoria
        letra = input("Digita uma letra: ").lower()

        if letra in alfabeto and len(letra) == 1: #verifica se o caractere existe na lista albeto[] e se é um unico caratere
            if letra in letras_adivinhadas or letra in letras_erradas: #Impedir a repetição de letras.
                print("Já digistaste essa letra, tenta outra!")
                continue
            # Verificar se a letra fornecida está presente na palavra secreta
            if letra in palavra_secreta:
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
                letras_erradas.append(letra)
                tentativas += 1
                desenhar_boneco(tentativas)

            # Atualizar a exibição da palavra com a letra revelada, se estiver correta
            print("Palavra: ", " ".join(letras_adivinhadas))

            # Verificar se o jogador venceu ou perdeu o jogo
            if "_" not in letras_adivinhadas:
                print("Parabéns!! Ganhaste \o/ \o/")
                return
        elif len(letra) == 1:
            print("Inválido. Apenas letras. Tente novamente.")
        else:
            print("Inválido. Digite uma única letra por favor.")

        print("Letras erradas: ", ", ".join(letras_erradas))

    print("Oh, não conseguiste! A palavra secreta era:", palavra_secreta,".Tenta outra vez!")

# Iniciar o jogo da forca
jogo_forca()
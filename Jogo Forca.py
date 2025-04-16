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


# Jogo Forca.py
import random
import boneco  # Importa o módulo de desenho

palavras = ["Ajuda", "Beato", "Areeiro", "Benfica", "Alvalade", "Marvila", "Campolide", "Lumiar", "Olivais"]
palavra_secreta = random.choice(palavras).lower()
letras_adivinhadas = ["_"] * len(palavra_secreta)
max_tentativas = 5
letras_erradas = []

def processar_letra(letra, palavra, letras_atualizadas):
    acertou = False
    for i, c in enumerate(palavra):
        if c == letra:
            letras_atualizadas[i] = letra.upper() if i == 0 else letra
            acertou = True
    return acertou

def jogo_forca():
    tentativas = 0
    print("***********  Olá, bem-vindo ao jogo da Forca! ***************")          
    print("Adivinha a palavra secreta.")
    print("Vamos dar-te uma dica, é uma das freguesias de Lisboa!")
    print("Tens 5 tentativas. Let's play :)")
    print("*************************************************************")
    print("Palavra:", " ".join(letras_adivinhadas))

    while tentativas < max_tentativas:
        letra = input("Digita uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in letras_adivinhadas or letra in letras_erradas:
                print("Já digitaste essa letra, tenta outra!")
                continue

            if processar_letra(letra, palavra_secreta, letras_adivinhadas):
                print("Parabéns, acertaste numa letra!")
            else:
                letras_erradas.append(letra)
                tentativas += 1
                boneco.desenhar_boneco(tentativas)  # ✅ Aqui chamamos a função
                print(f"Letra errada. Tentativas restantes: {max_tentativas - tentativas}")

            print("Palavra:", " ".join(letras_adivinhadas))

            if "_" not in letras_adivinhadas:
                print("Parabéns!! Ganhaste \o/ \o/")
                return
        else:
            print("Inválido. Digita uma única letra válida, por favor.")

        print("Letras erradas:", ", ".join(letras_erradas))

    print(f"Oh, não conseguiste! A palavra secreta era: {palavra_secreta.title()}. Tenta outra vez!")

# Iniciar o jogo
jogo_forca()



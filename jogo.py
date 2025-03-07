import random

def jogar():
    print(**********)
    print("Bem-vindos ao jogo de Adivinhação!")
    print(**********)

    numero_secreto = random.random(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dífícil")

    nivel = int(input("Defina o nível:"))

    if(nivel ==1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else(nivel==3):
        total_de_tentativas = 5
    #Loop de tentativas
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))   
    #Entrada do usuário
    chute_str = input("Digite um número entre 1 a 100!")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    #Validação de entrada
    if (chute < 1 or > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou)
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else 
        if (maior):
           print("Você errou! O seu chute foi maior do o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    print ("Fim de jogo!")

if(__name__=="__main__");
    jogar()    


import random #importa a biblioteca random, que nos permitirá randomizar as possibilidades do termo
from colorama import init, Fore #importa o init e o fore do colorama, que nos permitirá mudar as cores das letras

init(autoreset=True)

possibilidades = ["LETRA", "PONTE", "AMIGO", "XAMPU", "IMPAR", "JOGOS", "GRAÇA"]#possibilidades do termo
termo = random.choice(possibilidades)#aleatoriza uma das possibilidades para ser a palavra do chute
game_over = False#variável boleana que verifica se o jogador acertou a palavra ou perdeu
chances = 6#variavel da quantidade de chances do jogador

#imprime as instruções do jogo na tela do jogador
print("------------------------------------ INSTRUÇÕES ------------------------------------")
print("Você deve escolher uma palavra com até 05 letras (letras excedentes serão ignoradas)")
print(Fore.GREEN + "T" + Fore.RESET + "URMA -> a letra 'T' faz parte da palavra e está na posição correta")
print("VI" + Fore.YELLOW + "O" + Fore.RESET + "LA -> a letra 'O' faz parte da palavra mas em outra posição")
print("PUL" + Fore.RED + "G" + Fore.RESET + "A -> a letra 'G' não faz parte da palavra")
print("------------------------------------------------------------------------------------")

while not game_over:#enquanto o jogo não tiver acabado
    display = []#váriavel de lista, responsável por armazenar o chute com as cores de cada letra
    chute = str(input("Digite uma palavra com 5 letras: "))#pega o chute do usuário e armazena em uma váriavel
    chute = chute.upper()[:5]#separa as cinco primeiras letras do chute e as deixa em caixa alta
    chances -= 1#como o jogador chutou uma palavra, ele perde uma chance

    if chances == 0:#se o jogador já fez todos os chutes
        print("Acabaram as chances")#imprime a mensagem de derrota
        print("A palavra era:" + termo)#imprime a palavra correta
        game_over = True#encerra o loop

    elif chute == termo:#mas se o jogador acertou a palavra
        print("Parabéns, você acertou o termo!")#imprime a mensagem de vitória
        print(Fore.GREEN + chute + Fore.RESET)#imprime a palavra correta
        game_over = True#encerra o loop

    else:#se nenhuma das condições for respondida, significa que o jogador fez um chute mas não acertou a palavra
        for i in range(len(chute)):#cria um loop que passa por cada letra que o jogador inseriu
            if chute[i] == termo[i]:#se a letra do chute estiver no mesmo lugar que a letra do termo
                display.append(Fore.GREEN + chute[i] + Fore.RESET)#a letra está correta e é pintada da cor verde
            elif chute[i] in termo:#se a letra do chute estiver na palavra do termo
                display.append(Fore.YELLOW + chute[i] + Fore.RESET)#a letra está na palavra e é pintada da cor amarela
            else:#se não for nenhuma das alternativas acima, significa que a letra não está na palavra
                display.append(Fore.RED + chute[i] + Fore.RESET)#a letra não está na palavra e é pintada da cor verde

        print(''.join(display))#imprime na tela o chute do jogador com as cores de cada letra

input("Pressione Enter para fechar o jogo.")#ao pressionar qualquer tecla o jogo fecha






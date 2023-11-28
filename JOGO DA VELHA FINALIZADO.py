# Esse é o jogo da velha para jogar com duas pessoas

# Para jogar é simples, começa com o jogador inicial e tem que escolher um número para colocar em algum quadradinho como "1" e depois o outro jogador escolhe o outro número para colocar em outro quadradinho, e assim vai até alguém ganhar ou dar velha. 

# A fileira horizontal de baixo é 1, 2 e 3, e a do meio é 4, 5 e 6, e a de cima é 7, 8 e 9.

class JogoDaVelha: # define uma classe chamada 'JogoDaVelha'.
  tabuleiro = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '} # representa o tabuleiro do jogo como um dicionário, onde as chaves são as posições e os valores são os marcadores "X ou O".
  turno = None # O turno inicializa como 'None' e será usado para controlar de quem é o turno.

  def __init__(self, jogador_inicial="X"): 
      self.turno = jogador_inicial # unit é o construtor da classe. Ele inicializa uma instância da classe. o Jogador inicial é opcional, se não fornecido, é definido com X. Ele configura o turno inicial do jogador conforme especificado.

  def exibir_tabuleiro(self):
      print("┌───┬───┬───┐")
      print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
      print("├───┼───┼───┤")
      print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
      print("├───┼───┼───┤")
      print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
      print("└───┴───┴───┘") # é responsável por exibir visualmente o estado atual do tabuleiro do jogo usando arte ASCII.

  def verificar_jogada(self, jogada):
      if jogada in self.tabuleiro.keys():
          if self.tabuleiro[jogada] == " ":
              return True
      return False # Verifica se a jogada é válida ela recebe a posição da joga e retorna True se a posição estiver vazia, e false caso contrário.

  def verificar_tabuleiro(self): # verifica o estado atual do tabuleiro do jogo para determinar se há um vencedor ou se o jogo terminou em empate.
      # Verificações das 3 verticais
      if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
          return self.tabuleiro['7']
      elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
          return self.tabuleiro['8']
      elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
          return self.tabuleiro['9'] #Esta linha verifica se as posições 7, 4 e 1 no tabuleiro são ocupadas pelo mesmo símbolo X ou O e não são espaços em branco. A condição != ' 'garante que essas posições não estejam vazias. Se a condição for verdadeira, significa que a linha vertical da esquerda está preenchida com o mesmo símbolo, indicando que um jogador venceu na coluna esquerda do tabuleiro. Nesse caso, a função retorna o símbolo vencedor na posição '7'.

      # Verificações das 3 horizontais
      elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
          return self.tabuleiro['7']
      elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
          return self.tabuleiro['8']
      elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
          return self.tabuleiro['1']

      # Verificações das 2 diagonais
      elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
          return self.tabuleiro['7']
      elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
          return self.tabuleiro['1']

      # Verificando empate
      if [*self.tabuleiro.values()].count(' ') == 0: # usa o count para contar qunatas vexes o caractere de espaço em branco aparece nos valores do tabuleiro.
          return "empate"
      else: # Se a condição acima não for atendida, significa que ainda há espaços em branco no tabuleiro.
          return [*self.tabuleiro.values()].count(' ') # retorna o número de espaço em branco no tabuleiro.

  def jogar(self): # contém o loop principal do jogo. Ele exibe repetidamente o tabuleiro, solicita a jogada do jogador atual e atualiza o tabuleiro de acordo. O loop continua até que haja um vencedor ou o jogo termine em empate.

      while True:  # Este é um loop infinito que continuará executando até que seja explicitamente interrompido com uma instrução break. Isso cria um loop contínuo para o jogo.
          self.exibir_tabuleiro()

          print(f"Turno do {self.turno}, qual sua jogada?")

          while True: # Inicia outro loop infinito, desta vez para garantir que o jogador forneça uma execução válida.
              jogada = input("Jogada: ") # Solicita ao jogador que forneça uma jogada através da entrada do teclado.

              if self.verificar_jogada(jogada):  # Se a jogada for válida...
                  break  # Encerra o loop
              else: # executa quando a ação não é valida.
                  print(f"jogado do {self.turno} inválida, jogue novamente.")

          self.tabuleiro[jogada] = self.turno #  Se a jogar for válida, atribua a posição correspondente no tabuleiro ao símbolo do jogador atual (X ou O).

          estado = self.verificar_tabuleiro()

          if estado == "X": # verifica se o jogador X venceu.
              print("X é o vencedor!!!")
              break #  Encerra o loop principal do jogo, já que o jogo terminou.

          elif estado == "O": # Verifique se o jogador O venceu.
              print("O é o vencedor!!!")
              break

          if estado == "empate":
              print("EMPATE!!!")
              break

          # Troca o jogador do próximo turno
          self.turno = "X" if self.turno == "O" else "O"

      self.exibir_tabuleiro() #  Exibe o estado atual do tabuleiro após cada turno.

jogo = JogoDaVelha() # Uma instância da classe JogoDaVelha chamada jogo é criada.

jogo.jogar() # jogar da instância jogo é chamado para iniciar o jogo.
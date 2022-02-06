# Programa simples que simula um dado com valor máximo de 6 e mínimo de 1
   #Ideias futuras para o projeto:
        # * Poder trocar o valor maximo e mínimo do dado,
        # * Arrumar o menu para melhorar interação com o usuário,
        # * Tratar outros erros e exceções.

from random import randint
from time import sleep

class Simulador_dado:
    def __init__(self):
        self.num_max = 6
        self.num_min = 1
        self.mensagem = "Bem vindo ao simulador de dados, digite 'Sim' para jogar o dado e 'Não' para sair"

    def Jogar_dado(self):
        while True:
            try:
                resposta = input(self.mensagem).upper()
                if resposta == 'SIM' or resposta == 'S':
                    self.gerar_valor_dado()

                elif resposta == 'Não' or resposta == 'N' or resposta == 'NAO':
                    print("Obrigado!!")
                else:
                    print("Digite apenas 'Sim' ou 'Não'!")
            except:
                print("Ocorreu um erro inesparado")

    def gerar_valor_dado(self):
        valor_dado = randint(self.num_min, self.num_max)
        sleep(0.5)
        print("Rodando dado...")
        sleep(0.5)
        print(f"O valor tirado no dado foi: {valor_dado}!")
        sleep(1)



simulador = Simulador_dado()
simulador.Jogar_dado()

from services.busca_binaria import busca_binaria
from services.cores import VERMELHO, VERDE, RESET
from models.sala import Sala

class TerminalConsulta:
    """
    Interface de Terminal responsável por capturar as entradas e validações
    durante as consultas e buscas de registros escolares.
    """

    def __init__(self, sala):
        self.sala = sala

    def pedir_matricula(self, matricula=None):
        """
        Solicita a matrícula que se deseja pesquisar e garante que a entrada seja
        um número inteiro válido.
        
        Retorna:
            int: Número de matrícula digitado e validado.
        """

        print("\n" + "=" * 50)
        print("               PESQUISA DE MATRÍCULA              ")
        print("=" * 50)

        while True:

           
            while True:
                try:
                    valor = int(input("  -> Digite a matrícula do aluno (-1 para sair): "))
                    break
                except ValueError:
                    print(f"{VERMELHO}[ERRO] Matrícula inválida. Digite um número inteiro.{RESET}")
                            
            self.aluno = busca_binaria(self.sala.sala_aula, valor)

            if self.aluno is None and valor != -1:

                print(f"{VERMELHO}[ERRO] Aluno com matrícula informada não foi localizado!{RESET}")
                continue

            elif valor == -1:
                print(f"{VERDE}[SUCESSO] Saindo...{RESET}")
                self.aluno = None
                break
            else:

                print(f"{VERDE}[SUCESSO] Aluno encontrado!{RESET}")
                break
    

    def continuar_consulta(self):
        """
        Pergunta ao usuário se deseja realizar outra consulta de matrícula.

        Retorna:
            int: 0 para continuar consultando, 1 para encerrar o fluxo de consulta.
        """

        while True:

            opcao = input("Deseja consultar mais algum aluno (S/N)? ")
            if opcao.upper() == 'S':
                return 0
            elif opcao.upper() == 'N':
                return 1
            else:
                    print(f"{VERMELHO}[ERRO] Opção inválida. Digite S ou N.{RESET}")
                    continue


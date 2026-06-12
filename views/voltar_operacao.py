from models.sala import Sala
from services.cores import VERMELHO, VERDE, RESET

class VoltarOperacao:
    """
    Interface de Terminal responsável por gerenciar a operação de desfazer (Undo).
    Permite reverter a última ação de cadastro, edição ou remoção de alunos.
    """


    def __init__(self, sala):
        """
        Inicializa o controlador de desfazer associando a sala de aula ativa.
        
        Parâmetros:
            sala (Sala): Instância da sala que contém o histórico de operações.
        """
        self.sala = sala


    def verificacoes_iniciais(self):
        """
        Valida se há alguma operação na pilha para ser desfeita.
        Se houver, remove a operação do topo da pilha e a armazena localmente.
        
        Retorna:
            bool/None: Retorna True se a operação foi recuperada com sucesso,
                       ou None se a pilha estiver vazia.
        """
        # Verifica se o histórico de operações está vazio
        if len(self.sala.pilha_desfazer) == 0:
            print(f"{VERMELHO}Nenhuma operacao para desfazer!{RESET}")
            return None

        # Retira o registro de operação do topo da pilha (LIFO)
        self.operacao_aluno = self.sala.pilha_desfazer.pop()
        return True


    def volta_quem(self):
        """
        Executa o fluxo de reversão da operação recuperada.
        Pergunta ao usuário se ele confirma a ação e aplica a lógica de desfazer correspondente.
        """
        # Executa a verificação inicial para garantir que há algo a desfazer
        resultado = self.verificacoes_iniciais()

        # Se não houver operações, interrompe o fluxo
        if resultado is None:
            return None

        voltar_view = self.operacao_aluno
        
        # Loop de confirmação da ação do usuário
        while True:
            confirma = input(f"{VERMELHO}Tem certeza que deseja voltar uma operação? S/N: {RESET}").strip().upper()
            if confirma == "S" or confirma == "N":
                break
            else:
                print("Apenas S ou N")

        # Se o usuário desistir de desfazer, devolvemos a operação para a pilha
        if confirma == "N":
            self.sala.armazena_operacao(voltar_view)
            return

        # Desfazer CADASTRO: Remove o aluno que tinha sido inserido
        if voltar_view.tipo == "cadastrar":
            self.sala.sala_aula.remove(voltar_view.aluno)

        # Desfazer EDIÇÃO: Restaura todos os dados originais a partir da cópia salva
        elif voltar_view.tipo == "editar":
            voltar_view.aluno.nome = voltar_view.aluno_antigo.nome
            voltar_view.aluno.idade = voltar_view.aluno_antigo.idade
            voltar_view.aluno.curso = voltar_view.aluno_antigo.curso
            voltar_view.aluno.matricula = voltar_view.aluno_antigo.matricula
            # Reordena a lista porque a matrícula anterior pode afetar a ordenação
            self.sala.ordena_sala()

        # Desfazer REMOÇÃO: Insere o aluno novamente na lista e reordena
        elif voltar_view.tipo == "remover":
            self.sala.armazena_aluno(voltar_view.aluno)
            self.sala.ordena_sala()

        print(f"{VERDE}Operação revertida com sucesso!{RESET}")

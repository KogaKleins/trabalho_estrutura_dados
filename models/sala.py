class Sala:
    """
    Gerencia a coleção de alunos cadastrados na sala de aula.
    Responsável pelo armazenamento em Array (lista) e ordenação dos dados.
    
    Atributos:
        sala_aula (list): Lista contendo os objetos do tipo Aluno.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Sala com uma lista de alunos vazia.
        """
        self.sala_aula = []
        self.pilha_desfazer = []

    def armazena_operacao(self, operacao_aluno):
        """
        Registra uma operação na pilha de histórico para permitir desfazer ações.

        Parâmetros:
            operacao_aluno (OperacoesAlunos): Objeto com o tipo e estado anterior da operação.
        """
        self.pilha_desfazer.append(operacao_aluno)

    def armazena_aluno(self, aluno):
        """
        Adiciona um novo aluno ao array da sala de aula.

        Parâmetros:
            aluno (Aluno): Objeto Aluno a ser cadastrado.
        """
        self.sala_aula.append(aluno)

    def ordena_sala(self):
        """
        Ordena a lista de alunos (self.sala_aula) em ordem crescente de matrícula.
        Utiliza o algoritmo Bubble Sort otimizado com complexidade O(n^2).
        """
        n = len(self.sala_aula)  # Definindo o tamanho da lista
        for i in range(n):  # Bubble Sort
            # O limite 'n - i - 1' evita verificar novamente os elementos que já flutuaram para o final (ordenados)
            for j in range(0, n - i - 1):
                # Comparação entre o atributo matricula do aluno atual e do próximo
                if self.sala_aula[j].matricula > self.sala_aula[j + 1].matricula:
                    # Permuta (swap) os objetos inteiros de posição no array
                    self.sala_aula[j], self.sala_aula[j + 1] = self.sala_aula[j + 1], self.sala_aula[j]

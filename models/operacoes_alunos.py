class OperacoesAlunos:
    """
    Representa o registro de uma operação realizada sobre um Aluno.

    Utilizada pela pilha de desfazer (pilha_desfazer em Sala) para armazenar
    o histórico de modificações, permitindo futuramente reverter ações como
    cadastro, edição ou exclusão de alunos.

    Atributos:
        tipo (str): Tipo da operação realizada ('cadastrar', 'editar', 'remover').
        aluno (Aluno): Referência ao objeto Aluno sobre o qual a operação foi executada.
        aluno_antigo (Aluno, opcional): Cópia do objeto Aluno contendo o estado anterior antes de uma edição.
    """


    def __init__(self, tipo, aluno, aluno_antigo=None):
        """
        Inicializa um registro de operação com o tipo, o aluno e a cópia opcional do estado anterior.

        Parâmetros:
            tipo (str): Descrição do tipo de operação realizada.
            aluno (Aluno): Objeto Aluno que foi alvo da operação.
            aluno_antigo (Aluno, opcional): Cópia do objeto Aluno contendo o estado antes de ser editado.
        """
        self.tipo = tipo
        self.aluno = aluno
        self.aluno_antigo = aluno_antigo

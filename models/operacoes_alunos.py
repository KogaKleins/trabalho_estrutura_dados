class OperacoesAlunos:
    """
    Representa o registro de uma operação realizada sobre um Aluno.

    Utilizada pela pilha de desfazer (pilha_desfazer em Sala) para armazenar
    o histórico de modificações, permitindo futuramente reverter ações como
    cadastro, edição ou exclusão de alunos.

    Atributos:
        tipo (str): Tipo da operação realizada. Exemplos: 'cadastrar', 'editar', 'excluir'.
        aluno (Aluno): Referência ao objeto Aluno sobre o qual a operação foi executada.
    """

    def __init__(self, tipo, aluno):
        """
        Inicializa um registro de operação com o tipo e o aluno associado.

        Parâmetros:
            tipo (str): Descrição do tipo de operação realizada.
            aluno (Aluno): Objeto Aluno que foi alvo da operação.
        """
        self.tipo = tipo
        self.aluno = aluno

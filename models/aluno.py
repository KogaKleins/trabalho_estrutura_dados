class Aluno:
    """
    Representa a entidade de um estudante no sistema escolar.
    
    Atributos:
        nome (str): Nome completo do aluno.
        idade (int): Idade do aluno.
        curso (str): Nome do curso matriculado.
        matricula (int): Código identificador único de matrícula do aluno.
    """

    def __init__(self, nome, idade, curso, matricula):
        """
        Inicializa uma nova instância da classe Aluno.
        """
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula

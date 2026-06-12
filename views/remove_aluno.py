from services.cores import VERMELHO, VERDE, RESET


class DeleteAluno:
    """
    Interface de Terminal responsável por confirmar e executar
    a remoção de um aluno da lista da sala de aula.
    """

    def __init__(self, sala, aluno):
        """
        Inicializa a interface de exclusão com a sala e o aluno alvo.

        Parâmetros:
            sala (Sala): Instância da sala que contém a lista de alunos.
            aluno (Aluno): Objeto Aluno a ser removido.
        """
        self.sala = sala
        self.aluno = aluno

    def remove_aluno(self):
        """
        Solicita confirmação do usuário e, se confirmado, remove o aluno da lista.

        Retorna:
            int: 0 se o aluno foi removido com sucesso, 1 se o usuário cancelou.
        """
        while True:
            confirma = input(f"{VERMELHO}Tem certeza que deseja excluir o aluno? S/N: {RESET}").strip().upper()
            if confirma == "S" or confirma == "N":
                break
            else:
                print("Apenas S ou N.")

        if confirma == "S":
            self.sala.sala_aula.remove(self.aluno)
            print(f"{VERDE}Aluno removido com sucesso!{RESET}")
            return 0
        else:
            return 1
class EdicaoCadastro:
    """
    Interface de Terminal responsável por capturar e validar as entradas
    do usuário durante o processo de edição de dados de um Aluno já cadastrado.

    Atributos:
        aluno (Aluno): Referência ao objeto Aluno cujos dados serão modificados.
    """

    def __init__(self, aluno):
        """
        Inicializa a interface de edição com o aluno a ser modificado.

        Parâmetros:
            aluno (Aluno): Objeto Aluno que terá seus atributos editados.
        """
        self.aluno = aluno

    def opcao(self):
        """
        Exibe o menu de campos editáveis e captura a escolha do usuário.

        Garante que a entrada seja um número inteiro entre 1 e 4,
        correspondendo ao campo que o usuário deseja alterar.

        Retorna:
            int: Número da opção selecionada (1=Nome, 2=Idade, 3=Curso, 4=Matrícula).
        """
        print("Digite o numero da caracteristica que deseja alterar: ")
        print("1. Nome")
        print("2. Idade")
        print("3. Curso")
        print("4. Matrícula")
        while True:
            try:
                opcao = int(input("opção: "))
                if opcao < 1 or opcao > 4:
                    print("[ERRO] Opção inválida. Digite um número entre 1 e 4.")
                else:
                    break
            except ValueError:
                print("[ERRO] Entrada inválida. Digite um número inteiro.")
        return opcao

    def editar_nome(self):
        """
        Solicita e valida a entrada de um novo nome para o aluno.

        Garante que o campo não seja enviado vazio.

        Retorna:
            str: Novo nome do aluno em letras minúsculas, sem espaços extras.
        """
        while True:
            try:
                novo_nome = str(input("Digite o novo nome do aluno: ")).strip().lower()
                if novo_nome == "":
                    print("[ERRO] Nome inválido. Digite um nome para continuar.")
                else:
                    break
            except ValueError:
                print("[ERRO] Entrada inválida. Digite um nome para continuar.")
                
        return novo_nome

    def editar_idade(self):
        """
        Solicita e valida a entrada de uma nova idade para o aluno.

        Garante que a idade seja um inteiro positivo dentro do intervalo [0, 100].

        Retorna:
            int: Nova idade validada do aluno.
        """
        while True:
            try:
                nova_idade = int(input("Digite a nova idade do aluno: "))
                if nova_idade < 0 or nova_idade > 100:
                    print("[ERRO] Idade inválida. Digite um número entre 0 e 100.")
                else:
                    break
            except ValueError:
                print("[ERRO] Entrada inválida. Digite um número inteiro.")

        return nova_idade

    def editar_curso(self):
        """
        Solicita e valida a entrada de um novo curso para o aluno.

        Garante que o campo não seja enviado vazio.

        Retorna:
            str: Novo nome do curso em letras minúsculas, sem espaços extras.
        """
        while True:
            try:
                novo_curso = str(input("Digite o novo curso do aluno: ")).strip().lower()
                if novo_curso == "":
                    print("[ERRO] Curso inválido. Digite um curso para continuar.")
                else:
                    break
            except ValueError:
                print("[ERRO] Entrada inválida. Digite um curso para continuar.")

        return novo_curso

    def editar_matricula(self):
        """
        Solicita e valida a entrada de uma nova matrícula para o aluno.

        Garante que a entrada seja um valor inteiro válido.

        Retorna:
            int: Novo número de matrícula validado.
        """
        while True:
            try:
                nova_matricula = int(input("Digite a nova matrícula do aluno: "))
                break
            except ValueError:
                print("[ERRO] Entrada inválida. Digite um número inteiro.")

        return nova_matricula

    def continuar_edicao(self):
        """
        Pergunta ao usuário se deseja continuar realizando edições.

        Retorna:
            int: 0 para continuar editando, 1 para encerrar o fluxo de edição.
        """
        while True:
            opcao = input("Deseja continuar editando (S/N)? ")
            if opcao.upper() == 'S':
                return 0
            elif opcao.upper() == 'N':
                return 1
            else:
                print("[ERRO] Opção inválida. Digite S ou N.")

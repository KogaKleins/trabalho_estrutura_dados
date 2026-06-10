from services.cores import VERMELHO, VERDE, RESET

class TerminalCadastro:
    """
    Interface de Terminal responsável por capturar as entradas e validações de dados
    durante o processo de cadastro de novos alunos.
    """

    def quantidade_alunos(self):
        """
        Solicita a quantidade de alunos que o usuário deseja cadastrar em lote.
        Garante que a entrada seja um número inteiro positivo.
        
        Retorna:
            int: Quantidade de alunos a serem cadastrados.
        """
        print("\n" + "=" * 50)
        print("             CADASTRO DE NOVOS ALUNOS             ")
        print("=" * 50)
        
        while True:
            try:
                quant_aluno = int(input("Digite a quantidade de alunos que deseja cadastrar: "))
                if quant_aluno < 0:
                    print(f"{VERMELHO}[ERRO] Quantidade inválida. Digite um número positivo.{RESET}")
                else:
                    return quant_aluno
            except ValueError:
                print(f"{VERMELHO}[ERRO] Entrada inválida. Digite um número inteiro.{RESET}")

    def imprime_contador(self, i, quant):
        """
        Imprime o contador de alunos que estão sendo cadastrados.
        
        Parâmetros:
            i (int): Índice do aluno atual.
            quant (int): Quantidade total de alunos a serem cadastrados.
        """
        print(f"\n--- Cadastrando Aluno {i+1} de {quant} ---")

    def cadastrar_aluno(self):
        """
        Solicita, valida e captura individualmente os atributos de um Aluno.
        Garante que todas as entradas estejam devidamente tratadas.
        
        Retorna:
            tuple: Uma tupla contendo (nome, idade, curso, matricula).
        """
        # Entrada do Nome (Não pode ser vazio)
        while True:
            nome_aluno = str(input("  -> Digite o nome do aluno: ")).strip().lower()
            if nome_aluno == "":
                print(f"     {VERMELHO}[ERRO] Nome inválido. Digite um nome para continuar.{RESET}")
            else:
                break
        
        # Entrada da Idade (Valida intervalo realista de 0 a 100)
        while True:
            try:
                idade_aluno = int(input("  -> Digite a idade do aluno: "))
                if idade_aluno < 0 or idade_aluno > 100:
                    print(f"     {VERMELHO}[ERRO] Idade inválida. Digite um número entre 0 e 100.{RESET}")
                else:
                    break
            except ValueError:
                print(f"     {VERMELHO}[ERRO] Idade inválida. Digite um número inteiro.{RESET}")

        # Entrada do Curso (Não pode ser vazio)
        while True:
            curso_aluno = str(input("  -> Digite o curso do aluno: ")).strip().lower()
            if curso_aluno == "":
                print(f"     {VERMELHO}[ERRO] Curso inválido. Digite um nome de curso para continuar.{RESET}")
            else:
                break

        # Entrada da Matrícula (Garante que seja um valor inteiro)
        while True:
            try:
                matricula_aluno = int(input("  -> Digite a matrícula do aluno: "))
                break   
            except ValueError:
                print(f"     {VERMELHO}[ERRO] Matrícula inválida. Digite um número inteiro.{RESET}")

        print(f"{VERDE}[SUCESSO] Aluno cadastrado com sucesso!{RESET}\n")

        return nome_aluno, idade_aluno, curso_aluno, matricula_aluno

"""
Utilitário de Exibição de Dados para Terminal (views)

Contém funções de exibição reutilizáveis por qualquer classe da camada de View,
evitando duplicação de código de apresentação e respeitando o princípio DRY
(Don't Repeat Yourself).
"""

from services.cores import VERMELHO, VERDE, RESET


def imprime_aluno(aluno):
    """
    Exibe os dados completos de um Aluno formatados no terminal.

    Formata os campos de texto com capitalização (title case) para melhor
    legibilidade. Exibe uma mensagem de sucesso e os dados do aluno entre
    linhas divisórias visuais.

    Parâmetros:
        aluno (Aluno): Objeto Aluno cujos dados serão exibidos.
                       Se None, nada é exibido além da linha divisória inicial.
    """
    print("\n" + "-" * 50)
    if aluno is not None:
        print(f"{VERDE}[SUCESSO] Operação concluida com sucesso!{RESET}")
        print("-" * 50)
        # Capitaliza nome e curso para exibição padronizada
        print(f"  Nome      : {aluno.nome.title()}")
        print(f"  Idade     : {aluno.idade} anos")
        print(f"  Curso     : {aluno.curso.title()}")
        print(f"  Matrícula : {aluno.matricula}")
        print("-" * 50 + "\n")

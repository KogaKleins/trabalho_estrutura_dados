def busca_binaria(lista, valor):
    """
    Realiza a busca binária de um valor de matrícula dentro de uma lista ordenada de alunos.

    A busca binária exige que a lista esteja pré-ordenada. A cada iteração,
    o espaço de busca é reduzido à metade, resultando em complexidade O(log n),
    muito mais eficiente que a busca linear O(n) para grandes volumes de dados.

    Parâmetros:
        lista (list): Lista de objetos do tipo Aluno, ordenada por matrícula (crescente).
        valor (int): O número de matrícula a ser localizado.

    Retorna:
        Aluno: O objeto Aluno cuja matrícula coincide com o valor buscado.
        None: Caso o aluno não seja encontrado na lista.
    """
    inicio = 0           # Índice do primeiro elemento do intervalo de busca
    fim = len(lista) - 1 # Índice do último elemento do intervalo de busca

    while inicio <= fim:
        meio = (inicio + fim) // 2 # Ponto central do intervalo atual

        if lista[meio].matricula == valor:
            # Matrícula encontrada no meio: retorna o aluno diretamente
            return lista[meio]

        elif lista[meio].matricula < valor:
            # O valor buscado é maior: descarta a metade esquerda
            inicio = meio + 1
        else:
            # O valor buscado é menor: descarta a metade direita
            fim = meio - 1

    # Esgotou o intervalo sem encontrar: aluno não cadastrado
    return None

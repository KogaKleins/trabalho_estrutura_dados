class FilaAtendimento:
    """
    Gerencia as solicitações de atendimento da secretaria em ordem FIFO.
    """

    def __init__(self):
        self.solicitacoes = []

    def adicionar(self, nome, servico):
        """
        Adiciona uma nova solicitação ao final da fila.
        """
        solicitacao = {
            "nome": nome,
            "servico": servico
        }
        self.solicitacoes.append(solicitacao)

    def atender_proximo(self):
        """
        Remove e retorna a primeira solicitação da fila.
        """
        if not self.solicitacoes:
            return None

        return self.solicitacoes.pop(0)

    def quantidade(self):
        """
        Retorna a quantidade de solicitações aguardando atendimento.
        """
        return len(self.solicitacoes)

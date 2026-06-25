from services.cores import AZUL, RESET, VERDE, VERMELHO


class TerminalFila:
    """
    Interface de terminal da fila de atendimento da secretaria.
    """

    def solicitar_atendimento(self):
        """
        Captura o nome da pessoa e o serviço solicitado.
        """
        print(f"\n{AZUL}--- ENTRAR NA FILA DE ATENDIMENTO ---{RESET}")

        while True:
            nome = input("Digite o nome da pessoa: ").strip()
            if nome:
                break
            print(f"{VERMELHO}[ERRO] O nome não pode ficar vazio.{RESET}")

        while True:
            servico = input("Digite o serviço desejado: ").strip()
            if servico:
                break
            print(f"{VERMELHO}[ERRO] O serviço não pode ficar vazio.{RESET}")

        return nome, servico

    def confirmar_entrada(self, posicao):
        print(
            f"{VERDE}[SUCESSO] Solicitação adicionada à fila. "
            f"Posição: {posicao}.{RESET}"
        )

    def exibir_atendimento(self, solicitacao, quantidade_restante):
        if solicitacao is None:
            print(f"\n{VERMELHO}[AVISO] A fila de atendimento está vazia.{RESET}")
            return

        print(f"\n{VERDE}--- PRÓXIMO ATENDIMENTO ---{RESET}")
        print(f"Nome: {solicitacao['nome']}")
        print(f"Serviço: {solicitacao['servico']}")
        print(f"Pessoas aguardando: {quantidade_restante}")

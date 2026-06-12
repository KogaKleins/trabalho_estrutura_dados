from services.cores import AZUL, RESET, NEGRITO, VERMELHO

class PainelAtendimento:
    """
    Interface de Terminal para o Painel de Atendimento da Secretaria.
    Exibe o menu de opções do sistema escolar.
    """

    def painel_atendimento(self):
        """
        Exibe o menu principal estilizado de atendimento e lê a opção selecionada pelo usuário.
        
        Retorna:
            int: Código da escolha do usuário validado entre 1 e 6.
        """
        print(f"\n{AZUL}+--------------------------------------------------+")
        print("|       PAINEL DE ATENDIMENTO - SECRETARIA        |")
        print(f"+--------------------------------------------------+{RESET}")
        print(f"  {NEGRITO}1.{RESET} Cadastrar um novo aluno")
        print(f"  {NEGRITO}2.{RESET} Consultar informações de um aluno")
        print(f"  {NEGRITO}3.{RESET} Atualizar informações de um aluno")
        print(f"  {NEGRITO}4.{RESET} Excluir um aluno")
        print(f"  {NEGRITO}5.{RESET} Voltar Operação")
        print(f"  {NEGRITO}6.{RESET} Sair do painel de atendimento")
        print(f"{AZUL}----------------------------------------------------{RESET}")

        while True:
            try:
                # Leitura e conversão da escolha
                escolha = int(input("Digite o número da opção desejada: "))
                if escolha < 1 or escolha > 6:
                    print(f"{VERMELHO}[ERRO] Escolha inválida. Digite um número inteiro entre 1 e 6.{RESET}")
                else: 
                    return escolha
            except ValueError:
                print(f"{VERMELHO}[ERRO] Entrada inválida. Digite um número inteiro correspondente à opção.{RESET}")

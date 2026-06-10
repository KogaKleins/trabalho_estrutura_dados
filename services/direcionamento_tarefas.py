from models.aluno import Aluno
from models.sala import Sala
from models.operacoes_alunos import OperacoesAlunos
from views.terminal_cadastro import TerminalCadastro
from views.terminal_consulta import TerminalConsulta
from views.edicao_cadastro import EdicaoCadastro
from views.utils import imprime_aluno


class DirecionamentoTarefas:
    """
    Classe de controle e roteamento (Controller) responsável por direcionar
    o fluxo de execução do sistema para as rotinas correspondentes a cada opção de escolha.
    
    Atributos:
        sala (Sala): Instância persistente de Sala que armazena os dados dos alunos.
    """

    def __init__(self, sala):
        """
        Inicializa o direcionador de tarefas passando a referência da sala de aula.
        """
        self.sala = sala

    def direcionar(self, escolha):
        """
        Roteia o fluxo da aplicação conforme a escolha do usuário no painel de atendimento.
        
        Parâmetros:
            escolha (int): Opção numérica selecionada no menu.
            
        Retorna:
            int: -1 se a opção selecionada for 'Sair' (para interromper o loop), None caso contrário.
        """
        # Opção 1: Cadastrar novos alunos
        if escolha == 1:

            cadastro_view = TerminalCadastro()
            quant = cadastro_view.quantidade_alunos()

            for i in range(quant):
                cadastro_view.imprime_contador(i, quant)
                nome, idade, curso, matricula = cadastro_view.cadastrar_aluno()
                aluno = Aluno(nome, idade, curso, matricula)
                operacao_aluno = OperacoesAlunos("cadastrar", aluno)
                self.sala.armazena_aluno(aluno)
                self.sala.armazena_operacao(operacao_aluno)
            # A ordenação ocorre apenas uma única vez após todas as inserções
            self.sala.ordena_sala() 

        # Opção 2: Consultar informações de um aluno
        elif escolha == 2:

            consulta_view = TerminalConsulta(self.sala)
    
            while True:
                consulta_view.pedir_matricula()
                if consulta_view.aluno is None:
                    break
                imprime_aluno(consulta_view.aluno)
                opcao = consulta_view.continuar_consulta()
                if opcao == 0:
                    continue
                else:
                    break

        # Opção 3: Edição de cadastro
        elif escolha == 3:

            consulta_view = TerminalConsulta(self.sala)
            consulta_view.pedir_matricula()
            if consulta_view.aluno is None:
                return None

            edita_view = EdicaoCadastro(consulta_view.aluno)
            opcao = edita_view.opcao()
            if opcao == 1:
                novo_nome = edita_view.editar_nome()
                consulta_view.aluno.nome = novo_nome

            elif opcao == 2:
                nova_idade = edita_view.editar_idade()
                consulta_view.aluno.idade = nova_idade

            elif opcao == 3:
                novo_curso = edita_view.editar_curso()
                consulta_view.aluno.curso = novo_curso

            elif opcao == 4:
                nova_matricula = edita_view.editar_matricula()
                consulta_view.aluno.matricula = nova_matricula

            operacao_aluno = OperacoesAlunos("editar", consulta_view.aluno)
            self.sala.armazena_operacao(operacao_aluno)
            self.sala.ordena_sala()
            imprime_aluno(consulta_view.aluno)
            
        # Opção 5: Encerrar sistema
        elif escolha == 5:
            return -1

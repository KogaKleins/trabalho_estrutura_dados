"""
Sistema de Cadastro Escolar (Ponto de Entrada Principal)

Responsável por instanciar a estrutura de persistência de dados (Sala),
inicializar as interfaces de controle e gerenciar o loop principal de atendimento.
"""

from models.sala import Sala 
from models.fila_atendimento import FilaAtendimento
from views.painel_atendimento import PainelAtendimento
from services.direcionamento_tarefas import DirecionamentoTarefas
from services.cores import AZUL, RESET

# Inicialização persistente da sala de aula e interfaces de controle
sala = Sala()
fila_atendimento = FilaAtendimento()
painel_principal = PainelAtendimento()
direciona = DirecionamentoTarefas(sala, fila_atendimento)

# Loop contínuo do sistema de atendimento
while True:
    # Exibe o menu principal e obtém a escolha validada do usuário
    escolha = painel_principal.painel_atendimento()
    
    # Executa a ação selecionada passando a referência da sala ativa
    resultado = direciona.direcionar(escolha)

    # Critério de parada: Opção 'Sair' retorna -1
    if resultado == -1:
        break

# O encerramento do sistema fica aqui, no ponto de entrada principal!
print(f"\n{AZUL}" + "=" * 50)
print("  SISTEMA ENCERRADO!")
print("=" * 50 + f"{RESET}\n")

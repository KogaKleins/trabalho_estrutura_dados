# Sistema de Cadastro Escolar

Sistema interativo de terminal desenvolvido para o gerenciamento de alunos, matrículas e atendimento de secretaria escolar. Elaborado como trabalho prático da disciplina de **Estrutura de Dados**.

---

## Arquitetura

O sistema é inspirado/adota o padrão **MVC (Model-View-Controller)**, separando responsabilidades em três camadas bem definidas:

```
                      ┌────────────────────────────┐
                      │          main.py           │
                      │  Ponto de entrada e loop   │
                      └─────────────┬──────────────┘
                                    │
                                    ▼
          ┌─────────────────────────────────────────────────────┐
          │                    VIEW  (views/)                   │
          │                                                     │
          │  painel_atendimento.py  →  Menu principal           │
          │  terminal_cadastro.py   →  Entrada de cadastro      │
          │  terminal_consulta.py   →  Busca por matrícula      │
          │  edicao_cadastro.py     →  Edição de dados          │
          │  remove_aluno.py        →  Confirmação de exclusão  │
          │  voltar_operacao.py     →  Desfazer operação (Undo) │
          │  terminal_fila.py       →  Atendimento da fila      │
          │  utils.py               →  Exibição compartilhada   │
          └────────────────────────┬────────────────────────────┘
                                   │  captura entrada / exibe saída
                                   ▼
          ┌─────────────────────────────────────────────────────┐
          │                CONTROLLER  (services/)              │
          │                                                     │
          │  direcionamento_tarefas.py  →  Roteia ações do menu │
          │  busca_binaria.py           →  Algoritmo de busca   │
          │  cores.py                   →  Constantes ANSI      │
          └────────────────────────┬────────────────────────────┘
                                   │  lê / escreve estado
                                   ▼
          ┌─────────────────────────────────────────────────────┐
          │                   MODEL  (models/)                  │
          │                                                     │
          │  aluno.py            →  Entidade: dados do aluno    │
          │  sala.py             →  Array de alunos + pilha     │
          │  fila_atendimento.py →  Fila de solicitações        │
          │  operacoes_alunos.py →  Registro de operação        │
          └─────────────────────────────────────────────────────┘
```

---

## Estrutura de Arquivos

```
Trabalho_SistemaEscolar/
│
├── main.py                      # Ponto de entrada e loop principal
│
├── models/
│   ├── aluno.py                 # Entidade Aluno (nome, idade, curso, matrícula)
│   ├── sala.py                  # Gerencia array de alunos e pilha de desfazer
│   ├── fila_atendimento.py      # Gerencia a fila FIFO da secretaria
│   └── operacoes_alunos.py      # Registro de operação para a pilha
│
├── views/
│   ├── painel_atendimento.py    # Menu principal interativo (8 opções)
│   ├── terminal_cadastro.py     # Captura e valida dados de cadastro
│   ├── terminal_consulta.py     # Captura matrícula e dispara busca binária
│   ├── edicao_cadastro.py       # Captura e valida dados de edição
│   ├── remove_aluno.py          # Confirmação e remoção de aluno da lista
│   ├── voltar_operacao.py       # Interface de desfazer (Undo) da última operação
│   ├── terminal_fila.py         # Entrada e atendimento de solicitações da fila
│   └── utils.py                 # Função utilitária de exibição de aluno
│
└── services/
    ├── direcionamento_tarefas.py  # Controller: roteia ações do menu
    ├── busca_binaria.py           # Algoritmo de busca binária
    └── cores.py                   # Constantes ANSI de cor para o terminal
```

---

## Fluxo de Execução

```
  Início
    │
    ▼
  Instanciar Sala, PainelAtendimento, DirecionamentoTarefas
    │
    ▼                               ┌────────────────────┐
  ┌─────────────────────────┐       │                    │
  │   Exibir menu principal │ ◄─────┘  (volta ao menu)   │
  └────────────┬────────────┘                            │
               │  usuário digita uma opção               │
               ▼                                         │
  ┌──────────────────────────────┐                       │
  │  DirecionamentoTarefas       │                       │
  │    .direcionar(escolha)      │                       │
  └──────────────┬───────────────┘                       │
                 │                                       │
        ┌────────┴────────┐                              │
        │                 │                              │
   opcao=1 → Cadastrar alunos ──────────────────────────►│
   opcao=2 → Consultar por matrícula ───────────────────►│
   opcao=3 → Editar dados do aluno ─────────────────────►│
   opcao=4 → Remover aluno ─────────────────────────────►│
   opcao=5 → Desfazer última operação ──────────────────►┘
   opcao=6 → Entrar na fila de atendimento ─────────────►│
   opcao=7 → Atender próxima pessoa da fila ────────────►│
   opcao=8 → Retorna -1
                 │
                 ▼
        Encerramento do sistema
```

---

## Estruturas de Dados

### Array (Lista Python)
Armazenamento principal dos alunos no atributo `sala_aula` da classe `Sala`.  
Após cada inserção, edição de matrícula ou remoção revertida, a lista é reordenada com Bubble Sort para manter a invariante da busca binária.

### Pilha de Desfazer (`pilha_desfazer`)
Pilha implementada sobre lista Python no atributo `pilha_desfazer` da classe `Sala`.  
Cada operação realizada (cadastro, edição, remoção) registra um objeto `OperacoesAlunos` na pilha via `append()`. A operação de Desfazer retira o elemento do topo via `pop()` (LIFO) e reverte a ação correspondente.

| Tipo da operação | Estado salvo em `OperacoesAlunos`         | Ação de reversão                          |
|------------------|-------------------------------------------|-------------------------------------------|
| `"cadastrar"`    | Referência ao aluno inserido              | Remove o aluno da lista                   |
| `"editar"`       | Cópia manual do aluno antes da edição     | Restaura todos os campos do aluno original|
| `"remover"`      | Referência ao aluno excluído              | Reinserir o aluno e reordena a lista      |

### Fila de Atendimento (`FilaAtendimento`)
Armazena solicitações de atendimento da secretaria em uma lista Python. Novas
solicitações entram no final com `append()` e o próximo atendimento é retirado
do início com `pop(0)`, seguindo a ordem FIFO: primeiro a entrar, primeiro a sair.

---

## Algoritmos

### Bubble Sort — `Sala.ordena_sala()`

Ordena a lista `sala_aula` em ordem crescente de matrícula após cada inserção em lote, edição de matrícula ou reversão de remoção.  
Complexidade: **O(n²)**.

---

### Busca Binária — `busca_binaria(lista, valor)`

Localiza um aluno pela matrícula em uma lista já ordenada, dividindo o espaço de busca à metade a cada iteração.  
Complexidade: **O(log n)**.

> Requer que a lista esteja ordenada — garantido pelo Bubble Sort executado após cada modificação.

---

## Padrões de Projeto e Convenções

### Arquitetura MVC
- **Model:** entidades puras sem nenhuma lógica de apresentação (sem `print`).
- **View:** captura de entrada e exibição — nunca modifica diretamente os dados.
- **Controller (`DirecionamentoTarefas`):** orquestra a comunicação entre View e Model.

### Funções Puras como Utilitários
Funções que não guardam estado e podem ser reutilizadas por qualquer classe da mesma camada são definidas diretamente no nível do módulo, sem encapsulamento em classe desnecessário:
- `busca_binaria()` em `services/busca_binaria.py`
- `imprime_aluno()` em `views/utils.py`

### Convenções de Nomenclatura (PEP 8)
| Elemento         | Convenção   | Exemplo                    |
|------------------|-------------|----------------------------|
| Arquivos/módulos | `snake_case`| `terminal_cadastro.py`     |
| Classes          | `PascalCase`| `class TerminalCadastro:`  |
| Métodos          | `snake_case`| `def cadastrar_aluno(self)`|
| Variáveis locais | `snake_case`| `nome_aluno = ...`         |
| Constantes       | `UPPER_CASE`| `VERMELHO = "\033[31m"`    |

---

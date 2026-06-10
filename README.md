# Sistema de Cadastro Escolar

Sistema interativo de terminal desenvolvido para o gerenciamento de alunos, matrículas e atendimento de secretaria escolar. Elaborado como trabalho prático da disciplina de **Estrutura de Dados**.

---

## Arquitetura

O sistema adota o padrão **MVC (Model-View-Controller)**, separando responsabilidades em três camadas bem definidas:

```
┌─────────────────────────────────────────────────────────────┐
│                         main.py                             │
│              (Ponto de entrada — loop principal)            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   VIEW (views/)                             │
│                                                             │
│  painel_atendimento.py  ──►  Menu principal do terminal     │
│  terminal_cadastro.py   ──►  Entrada de dados de cadastro   │
│  terminal_consulta.py   ──►  Busca por matrícula            │
│  edicao_cadastro.py     ──►  Edição de dados do aluno       │
│  utils.py               ──►  Exibição compartilhada         │
└──────────────────────────┬──────────────────────────────────┘
                           │  captura entrada / exibe saída
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               CONTROLLER (services/)                        │
│                                                             │
│  direcionamento_tarefas.py ──► Orquestra o fluxo de dados   │
│  busca_binaria.py          ──► Algoritmo de busca           │
│  cores.py                  ──► Constantes de formatação     │
└──────────────────────────┬──────────────────────────────────┘
                           │  lê / escreve estado
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   MODEL (models/)                           │
│                                                             │
│  aluno.py            ──►  Entidade: dados de um estudante   │
│  sala.py             ──►  Array de alunos + pilha desfazer  │
│  operacoes_alunos.py ──►  Registro de operação (pilha)      │
└─────────────────────────────────────────────────────────────┘
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
│   └── operacoes_alunos.py      # Registro de operação para a pilha
│
├── views/
│   ├── painel_atendimento.py    # Menu principal interativo
│   ├── terminal_cadastro.py     # Captura e valida dados de cadastro
│   ├── terminal_consulta.py     # Captura matrícula e dispara busca
│   ├── edicao_cadastro.py       # Captura e valida dados de edição
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
  ▼
┌─────────────────────────┐
│  Exibir menu principal  │◄──────────────────────────────┐
└──────────┬──────────────┘                               │
           │ escolha do usuário                           │ (loop)
           ▼                                              │
  DirecionamentoTarefas.direcionar(escolha)               │
           │                                              │
    ┌──────┴──────┐                                       │
    │  escolha=1  │──► Cadastrar alunos ──────────────────┤
    │  escolha=2  │──► Consultar por matrícula ───────────┤
    │  escolha=3  │──► Editar dados de aluno ─────────────┘
    │  escolha=4  │──► (Em desenvolvimento)
    │  escolha=5  │──► Retorna -1
    └─────────────┘         │
                            ▼
                     Encerramento do sistema
```

---

## Estruturas de Dados

### Array (Lista Python)
Armazenamento principal dos alunos no atributo `sala_aula` da classe `Sala`.  
Após cada inserção ou edição de matrícula, a lista é reordenada com Bubble Sort para manter a invariante da busca binária.

### Pilha de Desfazer (`pilha_desfazer`)
Pilha implementada sobre lista Python no atributo `pilha_desfazer` da classe `Sala`.  
Cada operação realizada (cadastro, edição) registra um objeto `OperacoesAlunos` na pilha, permitindo futuramente reverter a última ação via `pop()`.

## Algoritmos

### Bubble Sort — `Sala.ordena_sala()`

Ordena a lista `sala_aula` em ordem crescente de matrícula após cada inserção ou edição.

---

### Busca Binária — `busca_binaria(lista, valor)`

Localiza um aluno pela matrícula em uma lista já ordenada, dividindo o espaço de busca à metade a cada iteração.

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

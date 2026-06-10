"""
Utilitário de Cores e Formatação para Terminal

Define constantes de escape ANSI para colorir e estilizar saídas no console de
forma limpa, evitando a poluição visual de caracteres ANSI misturados com o código de exibição.
"""

VERMELHO = "\033[31m" # 31 = Código ANSI para texto vermelho
VERDE = "\033[32m"    # 32 = Código ANSI para texto verde
AZUL = "\033[34m"     # 34 = Código ANSI para texto azul
RESET = "\033[0m"     # 0 = Código ANSI para resetar o texto
NEGRITO = "\033[1m"   # 1 = Código ANSI para texto em negrito

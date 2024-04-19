"""
Programa busca_sequencial.py
Descrisão: Este programa busca um valor em uma base de dados.
Gabriela RS
Versão: 0.0.2
Correção: Informação mais intuitiva de onde o cpf foi encontrado
Data: 19/04/2024
"""

## Alocação de memoria

lista = base
achou = False
posicao = 0

# leitura de dados 

cpf = int(input("Digite o valor a procurar:"))

print(cpf) # debug com print

# Saida de dados

if achou: 
    print(f'\nO valor {cpf} foi achado na {posicao + 1}.')
else: 
    print(f'\nO valor {cpf} não foi achado.')
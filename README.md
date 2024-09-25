# Sistema Bancário - Desafio DIO

## Descrição
Este projeto é um sistema bancário simples desenvolvido em Python como parte de um desafio da DIO. O objetivo é implementar as principais operações bancárias: depósito, saque e extrato. O sistema é projetado para um único usuário e não requer identificação de agência ou número de conta.

## Funcionalidades
- **Depósito:** Permite que o usuário deposite valores positivos na conta. Todos os depósitos são armazenados e exibidos no extrato.
- **Saque:** O sistema permite até 3 saques diários, com limite de R$ 500,00 por saque. Caso o saldo seja insuficiente, uma mensagem é exibida.
- **Extrato:** Exibe todos os depósitos e saques realizados, além do saldo atual da conta. Caso não haja movimentações, o sistema informa que não foram realizadas operações.

## Regras de Negócio
- O sistema trabalha com um saldo inicial de R$ 0,00.
- Limite de saque diário: 3 saques por dia, com valor máximo de R$ 500,00 por saque.
- Formatação monetária: os valores são exibidos no formato `R$ xxx.xx`.

## Tecnologias Utilizadas
- **Linguagem:** Python

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-dio.git

MENU = """
***************************************
**         BEM-VINDO AO BANCO DIO     **
***************************************

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
***************************************
=> """

saldo = 0
limite = 50
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("\nInforme o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("\n O valor informado é inválido.\n")
    
    elif opcao == "s":
        valor = float(input("\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n Saldo insuficiente.\n")

        elif excedeu_limite:
            print("\nO valor do saque excede o limite permitido.\n")

        elif excedeu_saques:
            print("\n Número máximo de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!\n")

        else:
            print("\n O valor informado é inválido.\n")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("========================================\n")

    elif opcao == "q":
        print("\nEncerrando o programa. Obrigado por utilizar o Banco DIO!\n")
        break

    else:
        print("\n Opção inválida. Por favor, selecione novamente.\n")

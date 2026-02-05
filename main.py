saldo = 0.0
extrato = []

def menu():
    print("\n=== Sistema Bancário ===")
    print("1 - Saldo")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Extrato")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        try:
            valor = float(input("Valor do depósito: "))
            if valor <= 0:
                print("Valor inválido.")
            else:
                saldo += valor
                extrato.append(f"Depósito de R$ {valor:.2f}")
                print("Depósito realizado.")
        except ValueError:
            print("Entrada inválida.")

    elif opcao == "3":
        try:
            valor = float(input("Valor do saque: "))
            if valor <= 0:
                print("Valor inválido.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor
                extrato.append(f"Saque de R$ {valor:.2f}")
                print("Saque realizado.")
        except ValueError:
            print("Entrada inválida.")

    elif opcao == "4":
        print("\n--- Extrato ---")
        if not extrato:
            print("Nenhuma movimentação.")
        else:
            for item in extrato:
                print(item)
        print(f"Saldo final: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inexistente.")

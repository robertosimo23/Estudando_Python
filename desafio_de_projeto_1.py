menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100.300
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

while True:

    opcao = input(menu)

    if opcao == "d":
        valor=float(input("Informe o valor do deposito:"))

        if valor + 0:
            saldo +=valor
            extrato += f"Deposito de R$ {valor:.2f}\n"
        else:
            print("Operação de Deposito falhou!\n O valor informado é inválido.")

    elif opcao == "s":
        valor = float (input("Informe o valor de saque:"))
        excedeu_saldo=valor>saldo
        excedeu_limite=valor>limite 
        excedeu_saques= numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! O usuário não possui Saldo Suficiente ,ou seja, VC È LISO")
        elif excedeu_limite:
            print("Operação falhou ! O valor do saque excede o limite diário.")

        elif valor>0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques+= 1
        else:
            print( "Operação falou! valor informado é inválido")
        
    elif opcao == "e":
        print("\n ==================== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo: .2f}")
        print("=========================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida ,por favor novamente a operação desejada")

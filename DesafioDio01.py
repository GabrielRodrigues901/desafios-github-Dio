menu = input("Bem vindo ao Maze Bank.O que voce deseja fazer:1-Depositar  2-Sacar  3-Extrato 4-Sair ")
total = 0
saldo = 1000
extrato = f"Seu Saldo:{saldo} reais"
limite = 500

Numero_Saques = 0
Limite_Saques = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto voce deseja depositar?"))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else:
            print("Operação Falha.Tente denovo")

    elif opcao == "2":
       valor = float(input("Informe o valor de saque: "))
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saque = Numero_Saques >= Limite_Saques

       if excedeu_saldo:
           print("Operação falhou! você nao tem saldo suficiente")
       elif excedeu_limite:
           print("Operação falhou! o valor do saque excedeu o limite")
       elif excedeu_saque:
           print("Operação falhou! Numero de saques foi excedido")
       elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
       else:
           print("Operação falhou! o valor informado é invalido")


    elif opcao == "3":
        print("Extrato")
        print("Não foram realizados movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Ate mais")
        break
    else:
        print("Operação Invalida,tente denovo")

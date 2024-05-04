menu = """"
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do deposito:"))
        if valor >= 0 :
            saldo+= valor
            extrato+= f"Deposito: R${valor:.2f}\n"
        
        elif valor < 0:
            print("Operação falhou! O valor informado é inválido.")
            break
            
    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saque maior que o saldo disponivel")

        elif excedeu_limite:
            print("Operação falhou! Valor acima do limite de saque")
        
        elif excedeu_limite_saques:
            print("Operação falhou! Numero máximo de saques atingido")

        elif valor>0:
            saldo-= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Valor invalido")

    elif opcao == "e":
        print("Extrato")
        print(f"-----Extrato-----")
        print("Não foi realizado movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"-----------------")


    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
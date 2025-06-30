import time

menu="""
===============================
 Olá! Seja bem-vindo ao nosso banco.
 Escolha uma das opções abaixo:
[0]=Sacar
[1]=Depositar
[2]=Extrato
[3]=Sair
Digite a opção desejada:
=============================== 
"""
saldo=0
limite= 500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:

    opcao= input(menu)

    if opcao == "0":
        valor= float(input(" Informe o valor do saque: "))

        excedeu_saldo =valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques>= LIMITE_SAQUES

        if excedeu_saldo:
            print("TRANSAÇÃO NÃO AUTORIZADA. SALDO INSUFICIENTE.")

        elif excedeu_limite:
            print("LIMITE DIÁRIO EXCEDIDO. " )

        elif excedeu_saques:
            print("VALOR EXCEDE O LIMITE DE SAQUE.")

        elif valor  > 0:
            saldo -= valor
            extrato += ("SAQUE: R$ {:.2f}\n ".format(valor))
            numero_saques += 1


            print("AGUARDE A CONTAGEM DAS CÉDULAS.....")
            time.sleep(2)
            
            print("CONTANDO.....")
            time.sleep(2)

            print("RETIRE SEU DINHEIRO. OBRIGADO POR USAR NOSSO BANCO!")

    elif opcao =="1":

        valor = float(input("INFORME O VALOR DO DEPÓSITO:"))
        if valor > 0:
            saldo += valor
            extrato += ("DEPÓSITO: R$ {:.2f}\n".format(valor))

        else:
            print("O VALOR INFORMADO E INVÁLIDO.")

    elif opcao =="2":
        extratoP="EXTRATO"
        print(extratoP.center(50,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("Saldo: R$ {:.2f}".format(saldo))
        print("".center(50,"="))

    elif opcao == "3":
        print("Saindo... Obrigado por usar nosso banco. Até logo!")
        break

    else:
        print("OPÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA. ")

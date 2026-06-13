# MULTICALCULADORA

# Variável que indica qual calculadora está selecionada
calculadora_atual = "basica"

# LOOP PRINCIPAL

while True:

    # MENU SUPERIOR

    print("=====================================")
    print(" CALCULADORA DE TROCO")
    print(" CALCULADORA BÁSICA")
    print(" CALCULADORA DE RESISTÊNCIA")
    print("=====================================")

    print(f"\nCalculadora selecionada: {calculadora_atual}")

    # ESCOLHA DA CALCULADORA

    print("\n1 - Troco")
    print("2 - Básica")
    print("3 - Resistência")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    # ENCERRAR PROGRAMA

    if opcao == "0":
        break

    # CALCULADORA DE TROCO

    elif opcao == "1":

        calculadora_atual = "troco"

        print("\n=== CALCULADORA DE TROCO ===")

        # FUTURAMENTE:
        # pedir valor da compra
        # pedir valor pago
        # calcular troco
        # mostrar notas e moedas

        input("\nPressione ENTER...")

    # CALCULADORA BÁSICA

    elif opcao == "2":

        calculadora_atual = "basica"

        print("\n=== CALCULADORA BÁSICA ===")

        try:

            resultado = float(
                input("\nPrimeiro número: ")
            )

            while True:

                operacao = input(
                    "\nOperação (+, -, *, /) ou S para sair: "
                )

                if operacao.upper() == "S":
                    break

                numero = float(
                    input("Próximo número: ")
                )

                if operacao == "+":
                    resultado += numero

                elif operacao == "-":
                    resultado -= numero

                elif operacao == "*":
                    resultado *= numero

                elif operacao == "/":
                    resultado /= numero

                else:
                    print("\nOperação inválida.")
                    continue

                print(f"\nResultado atual: {resultado}")

        except ValueError:
            print("\nDigite apenas números.")

        except ZeroDivisionError:
            print("\nNão é possível dividir por zero.")

        input("\nPressione ENTER...")

    # CALCULADORA DE RESISTÊNCIA

    elif opcao == "3":

        calculadora_atual = "resistencia"

        print("\n=== CALCULADORA DE RESISTÊNCIA ===")

        # FUTURAMENTE:
        # escolher série ou paralelo
        # informar resistores
        # calcular resistência equivalente

        input("\nPressione ENTER...")

    # OPÇÃO INVÁLIDA

    else:

        print("\nOpção inválida.")
        input("\nPressione ENTER...")
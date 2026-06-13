# MULTICALCULADORA

# Variável que indica qual calculadora está selecionada
calculadora_atual = "basica"

# LOOP PRINCIPAL

while True:

    print("\n" * 50)

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
        print("\nEncerrando programa...")
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

        while True:

            print("\n" * 50)
            print("=== CALCULADORA BÁSICA ===")
            print("Digite S para voltar ao menu.\n")
            # PRIMEIRO NÚMER

            while True:

                entrada = input("Primeiro número: ")

                if entrada.upper() == "S":
                    break

                try:

                    resultado = float(entrada)
                    break

                except ValueError:

                    print("Digite um número válido.")

            if entrada.upper() == "S":
                break
            # LOOP DE OPERAÇÕE

            while True:

                operacao = input(
                    "\nOperação (+, -, *, /) ou S para sair: "
                )

                if operacao.upper() == "S":
                    break

                if operacao not in ["+", "-", "*", "/"]:

                    print("Operação inválida.")
                    continue

                # PRÓXIMO NÚMERO

                while True:

                    try:

                        numero = float(
                            input("Próximo número: ")
                        )

                        break

                    except ValueError:

                        print("Digite um número válido.")

                # CÁLCULOS

                if operacao == "+":
                    resultado += numero

                elif operacao == "-":
                    resultado -= numero

                elif operacao == "*":
                    resultado *= numero

                elif operacao == "/":

                    if numero == 0:

                        print(
                            "Não é possível dividir por zero."
                        )

                        continue

                    resultado /= numero

                print(
                    f"\nResultado atual: {resultado}"
                )

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
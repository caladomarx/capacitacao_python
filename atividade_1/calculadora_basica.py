def calculadora_basica():

    while True:

        print("\n" * 50)
        print("=== CALCULADORA BÁSICA ===")
        print("Digite S para voltar ao menu.\n")

        while True:

            entrada = input(
                "Primeiro número: "
            )

            if entrada.upper() == "S":
                return

            try:

                resultado = float(
                    entrada
                )

                break

            except ValueError:

                print(
                    "Digite um número válido."
                )

        while True:

            operacao = input(
                "\nOperação (+, -, *, /) ou S para sair: "
            )

            if operacao.upper() == "S":
                return

            if operacao not in [
                "+",
                "-",
                "*",
                "/"
            ]:

                print(
                    "Operação inválida."
                )

                continue

            while True:

                try:

                    numero = float(
                        input(
                            "Próximo número: "
                        )
                    )

                    break

                except ValueError:

                    print(
                        "Digite um número válido."
                    )

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
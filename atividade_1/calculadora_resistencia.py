def calculadora_resistencia():

    print(
        "\n=== CALCULADORA DE RESISTÊNCIA ==="
    )

    while True:

        print("\n1 - Série")
        print("2 - Paralelo")

        tipo = input(
            "\nEscolha: "
        )

        if tipo in ["1", "2"]:
            break

        print("Opção inválida.")

    while True:

        try:

            quantidade = int(
                input(
                    "\nQuantidade de resistores: "
                )
            )

            if quantidade < 2:

                print(
                    "Informe pelo menos 2 resistores."
                )

                continue

            break

        except ValueError:

            print(
                "Digite um número inteiro válido."
            )

    resistores = []

    for i in range(quantidade):

        while True:

            try:

                resistor = float(
                    input(
                        f"R{i + 1} (Ω): "
                    )
                )

                if resistor <= 0:

                    print(
                        "O valor deve ser maior que zero."
                    )

                    continue

                resistores.append(
                    resistor
                )

                break

            except ValueError:

                print(
                    "Digite um valor válido."
                )

    if tipo == "1":

        resistencia_equivalente = sum(
            resistores
        )

    else:

        soma_inversos = 0

        for resistor in resistores:

            soma_inversos += (
                1 / resistor
            )

        resistencia_equivalente = (
            1 / soma_inversos
        )

    print(
        f"\nResistência equivalente: "
        f"{resistencia_equivalente:.2f} Ω"
    )

    input("\nPressione ENTER...")
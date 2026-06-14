def calculadora_troco():

    print("\n=== CALCULADORA DE TROCO ===")

    while True:

        try:

            compra = float(
                input("\nValor da compra: R$ ")
            )

            break

        except ValueError:

            print("Digite um valor válido.")

    while True:

        try:

            pago = float(
                input("Valor pago: R$ ")
            )

            if pago < compra:

                print(
                    "O valor pago deve ser maior ou igual ao valor da compra."
                )

                continue

            break

        except ValueError:

            print("Digite um valor válido.")

    compra_centavos = round(compra * 100)
    pago_centavos = round(pago * 100)

    troco_centavos = pago_centavos - compra_centavos

    troco = troco_centavos / 100

    print(f"\nTroco: R$ {troco:.2f}")

    notas = [
        20000,
        10000,
        5000,
        2000,
        1000,
        500,
        200
    ]

    print("\nNotas:")

    resto = troco_centavos

    for nota in notas:

        quantidade = resto // nota

        if quantidade > 0:

            texto = (
                "nota"
                if quantidade == 1
                else "notas"
            )

            print(
                f"{quantidade} {texto} de R$ {nota // 100}"
            )

            resto %= nota

    moedas = [
        100,
        50,
        25,
        10,
        5
    ]

    print("\nMoedas:")

    for moeda in moedas:

        quantidade = resto // moeda

        if quantidade > 0:

            texto = (
                "moeda"
                if quantidade == 1
                else "moedas"
            )

            print(
                f"{quantidade} {texto} de R$ {moeda / 100:.2f}"
            )

            resto %= moeda

    input("\nPressione ENTER...")
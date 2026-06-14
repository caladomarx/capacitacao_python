# MULTICALCULADORA

calculadora_atual = "basica"

# CALCULADORA DE TROCO

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

    # NOTAS

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

    # MOEDAS

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

# CALCULADORA BÁSICA

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

# CALCULADORA DE RESISTÊNCIA

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

# MENU PRINCIPAL

while True:

    print("\n" * 50)

    print("=====================================")
    print(" CALCULADORA DE TROCO")
    print(" CALCULADORA BÁSICA")
    print(" CALCULADORA DE RESISTÊNCIA")
    print("=====================================")

    print(
        f"\nCalculadora selecionada: "
        f"{calculadora_atual}"
    )

    print("\n1 - Troco")
    print("2 - Básica")
    print("3 - Resistência")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "0":

        print(
            "\nEncerrando programa..."
        )

        break

    elif opcao == "1":

        calculadora_atual = "troco"
        calculadora_troco()

    elif opcao == "2":

        calculadora_atual = "basica"
        calculadora_basica()

    elif opcao == "3":

        calculadora_atual = "resistencia"
        calculadora_resistencia()

    else:

        print("\nOpção inválida.")
        input("\nPressione ENTER...")

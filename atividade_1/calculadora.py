from calculadora_basica import calculadora_basica
from calculadora_troco import calculadora_troco
from calculadora_resistencia import calculadora_resistencia

calculadora_atual = "basica"

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
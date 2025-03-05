from queries import listar_servicos_por_data

def menu():
    while True:
        print("\n===== Sistema de Gerenciamento da Oficina Mecânica =====")
        print("1 - Listar serviços por data")
        print("2 - Listar veículos por cliente")
        print("3 - Listar clientes por funcionário")
        print("4 - Listar serviços por veículo")
        print("5 - Valor total das faturas por cliente")
        print("6 - Listar nome e contato dos funcionários")
        print("7 - Média do valor dos serviços")
        print("8 - Listar veículos atendidos por mês")
        print("9 - Listar total do caixa por período")
        print("10 - Listar dados de uma fatura específica")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1 - Listar serviços por data")
            break
        elif opcao == "2":
            print("2 - Listar veículos por cliente")
            break
        elif opcao == "3":
            print("3 - Listar clientes por funcionário")
            break
        elif opcao == "4":
            print("4 - Listar serviços por veículo")
            break
        elif opcao == "5":
            print("5 - Valor total das faturas por cliente")
            break
        elif opcao == "6":
            print("6 - Listar nome e contato dos funcionários")
            break
        elif opcao == "7":
            print("7 - Média do valor dos serviços")
            break
        elif opcao == "8":
            print("8 - Listar veículos atendidos por mês")
            break
        elif opcao == "9":
            print("9 - Listar total do caixa por período")
            break
        elif opcao == "10":
            print("10 - Listar dados de uma fatura específica")
            break
        elif opcao == "0":
            print("0 - Sair")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
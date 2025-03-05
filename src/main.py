from queries import (
    listar_servicos_por_data,
    listar_veiculos_por_cliente,
    listar_clientes_por_funcionario,
    listar_servicos_por_veiculo,
    valor_total_faturas_por_cliente,
    listar_nome_e_contato_dos_funcionarios,
    listar_media_do_valor_dos_servicos,
    listar_veiculos_atendidos_por_mes,
    listar_total_caixa_por_periodo,
    listar_dados_de_fatura,
)
import os


def prints():
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
    print("11 - Limpar Terminal")
    print("0 - Sair")


def menu():
    prints()

    while True:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1 - Listar serviços por data")
        elif opcao == "2":
            print("2 - Listar veículos por cliente")
            id_cliente = input("Digite o ID do cliente: ")
            veiculos = listar_veiculos_por_cliente(id_cliente)
            if veiculos:
                print("\nVeículos do cliente:")
                for veiculo in veiculos:
                    print(veiculo)
            else:
                print("Nenhum veículo encontrado para este cliente.")
        elif opcao == "3":
            print("3 - Listar clientes por funcionário")
        elif opcao == "4":
            print("4 - Listar serviços por veículo")
        elif opcao == "5":
            print("5 - Valor total das faturas por cliente")
        elif opcao == "6":
            print("6 - Listar nome e contato dos funcionários")
        elif opcao == "7":
            print("7 - Média do valor dos serviços")
        elif opcao == "8":
            print("8 - Listar veículos atendidos por mês")
        elif opcao == "9":
            print("9 - Listar total do caixa por período")
        elif opcao == "10":
            print("10 - Listar dados de uma fatura específica")
        elif opcao == "11":
            print("11 - Limpar")
            os.system('clear')
            prints()
        elif opcao == "0":
            print("0 - Sair")

            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()

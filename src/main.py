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
            data = input("Digite a data (YYYY-MM-DD): ")
            servicos = listar_servicos_por_data(data)
            if servicos:
                print("\nServiços realizados na data", data)
                for servico in servicos:
                    print(servico)
            else:
                print("Nenhum serviço encontrado para esta data.")

        elif opcao == "2":
            id_cliente = input("Digite o ID do cliente: ")
            veiculos = listar_veiculos_por_cliente(id_cliente)
            if veiculos:
                print("\nVeículos do cliente:")
                for veiculo in veiculos:
                    print(veiculo)
            else:
                print("Nenhum veículo encontrado para este cliente.")

        elif opcao == "3":
            id_funcionario = input("Digite o ID do funcionário: ")
            clientes = listar_clientes_por_funcionario(id_funcionario)
            if clientes:
                print("\nClientes atendidos pelo funcionário:")
                for cliente in clientes:
                    print(cliente)
            else:
                print("Nenhum cliente encontrado para este funcionário.")

        elif opcao == "4":
            placa = input("Digite a placa do veículo: ")
            servicos = listar_servicos_por_veiculo(placa)
            if servicos:
                print("\nServiços realizados para o veículo:", placa)
                for servico in servicos:
                    print(servico)
            else:
                print("Nenhum serviço encontrado para este veículo.")

        elif opcao == "5":
            id_cliente = input("Digite o ID do cliente: ")
            total = valor_total_faturas_por_cliente(id_cliente)
            print(f"\nValor total das faturas do cliente: R$ {total:.2f}")

        elif opcao == "6":
            funcionarios = listar_nome_e_contato_dos_funcionarios()
            print("\nNome e contato dos funcionários:")
            for funcionario in funcionarios:
                print(funcionario)

        elif opcao == "7":
            media = listar_media_do_valor_dos_servicos()
            print(f"\nMédia do valor dos serviços: R$ {media:.2f}")

        elif opcao == "8":
            mes = input("Digite o mês (1-12): ")
            ano = input("Digite o ano (YYYY): ")
            veiculos = listar_veiculos_atendidos_por_mes(mes, ano)
            if veiculos:
                print("\nVeículos atendidos no período:")
                for veiculo in veiculos:
                    print(veiculo)
            else:
                print("Nenhum veículo encontrado para este período.")

        elif opcao == "9":
            data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
            data_fim = input("Digite a data de fim (YYYY-MM-DD): ")
            total = listar_total_caixa_por_periodo(data_inicio, data_fim)
            print(f"\nTotal do caixa no período: R$ {total:.2f}")

        elif opcao == "10":
            id_fatura = input("Digite o ID da fatura: ")
            fatura = listar_dados_de_fatura(id_fatura)
            if fatura:
                print("\nDados da fatura:", fatura)
            else:
                print("Fatura não encontrada.")

        elif opcao == "11":
            print("11 - Limpar")
            os.system("cls" if os.name == "nt" else "clear")
            prints()
        elif opcao == "0":
            print("0 - Sair")

            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()

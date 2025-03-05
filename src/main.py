from queries import listar_servicos_por_data

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Gerenciamento da Oficina Mecânica!")
    data = input("Digite a data para listar os serviços (YYYY-MM-DD): ")
    listar_servicos_por_data(data)
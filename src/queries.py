from database_connection import connect


def listar_servicos_por_data(data):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT s.id_servico, s.descricao, s.valor, f.id_fatura, f.data
        FROM Servico_Fatura sf
        JOIN Servico s ON sf.id_servico = s.id_servico
        JOIN Fatura f ON sf.id_fatura = f.id_fatura
        WHERE f.data = %s
    """
    cursor.execute(query, (data,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_veiculos_por_cliente(id_cliente):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT id_veiculo, marca, modelo, ano, placa
        FROM Veiculo
        WHERE id_cliente = %s
    """
    cursor.execute(query, (id_cliente,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_clientes_por_funcionario(id_funcionario):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT DISTINCT c.id_cliente, c.nome, c.telefone, c.email
        FROM Cliente c
        JOIN Fatura f ON c.id_cliente = f.id_cliente
        JOIN Servico_Fatura sf ON f.id_fatura = sf.id_fatura
        WHERE sf.id_funcionario = %s
    """
    cursor.execute(query, (id_funcionario,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_servicos_por_veiculo(placa):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT s.id_servico, s.descricao, s.valor
        FROM Servico_Fatura sf
        JOIN Servico s ON sf.id_servico = s.id_servico
        JOIN Fatura f ON sf.id_fatura = f.id_fatura
        JOIN Cliente c ON f.id_cliente = c.id_cliente
        JOIN Veiculo v ON c.id_cliente = v.id_cliente
        WHERE v.placa = %s
    """
    cursor.execute(query, (placa,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def valor_total_faturas_por_cliente(id_cliente):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT SUM(valor_total) AS total_gasto
        FROM Fatura
        WHERE id_cliente = %s
    """
    cursor.execute(query, (id_cliente,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0


def listar_nome_e_contato_dos_funcionarios():
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT nome, telefone
        FROM Funcionario
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_media_do_valor_dos_servicos():
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT AVG(valor) AS media_servicos
        FROM Servico
    """
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0


def listar_veiculos_atendidos_por_mes(mes, ano):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT DISTINCT v.id_veiculo, v.marca, v.modelo, v.ano, v.placa
        FROM Fatura f
        JOIN Cliente c ON f.id_cliente = c.id_cliente
        JOIN Veiculo v ON c.id_cliente = v.id_cliente
        WHERE MONTH(f.data) = %s AND YEAR(f.data) = %s
    """
    cursor.execute(query, (mes, ano))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_total_caixa_por_periodo(data_inicio, data_fim):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT SUM(valor_total) AS total_caixa
        FROM Fatura
        WHERE data BETWEEN %s AND %s
    """
    cursor.execute(query, (data_inicio, data_fim))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0


def listar_dados_de_fatura(id_fatura):
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT f.id_fatura, f.data, f.valor_total, c.nome AS cliente, c.telefone, c.email
        FROM Fatura f
        JOIN Cliente c ON f.id_cliente = c.id_cliente
        WHERE f.id_fatura = %s
    """
    cursor.execute(query, (id_fatura,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

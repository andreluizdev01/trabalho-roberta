from database_connection import  connect

def listar_servicos_por_data(data):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT s.id_servico, s.descricao, s.valor
    FROM Servico s
    JOIN Servico_Fatura sf ON s.id_servico = sf.id_servico
    JOIN Fatura f ON sf.id_fatura = f.id_fatura
    WHERE f.data = %s;
    """
    cursor.execute(query, (data,))
    result = cursor.fetchall()
    conn.close()
    return result

def listar_veiculos_por_cliente(id_cliente):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT id_veiculo, marca, modelo, ano, placa
    FROM Veiculo
    WHERE id_cliente = %s;
    """
    cursor.execute(query, (id_cliente,))
    result = cursor.fetchall()
    conn.close()
    return result

def listar_clientes_por_funcionario(id_funcionario):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT DISTINCT c.id_cliente, c.nome, c.telefone, c.email
    FROM Cliente c
    JOIN Fatura f ON c.id_cliente = f.id_cliente
    WHERE f.id_cliente IN (
        SELECT DISTINCT id_cliente FROM Fatura
    );
    """
    cursor.execute(query, (id_funcionario,))
    result = cursor.fetchall()
    conn.close()
    return result

def listar_servicos_por_veiculo(placa):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT s.id_servico, s.descricao, s.valor
    FROM Servico s
    JOIN Servico_Fatura sf ON s.id_servico = sf.id_servico
    JOIN Fatura f ON sf.id_fatura = f.id_fatura
    JOIN Cliente c ON f.id_cliente = c.id_cliente
    JOIN Veiculo v ON c.id_cliente = v.id_cliente
    WHERE v.placa = %s;
    """
    cursor.execute(query, (placa,))
    result = cursor.fetchall()
    conn.close()
    return result

def valor_total_faturas_por_cliente(id_cliente):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT SUM(valor_total) AS total_gasto
    FROM Fatura
    WHERE id_cliente = %s;
    """
    cursor.execute(query, (id_cliente,))
    result = cursor.fetchone()
    conn.close()
    return result

def listar_nome_e_contato_dos_funcionarios():
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT nome, telefone
    FROM Funcionario;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def listar_media_do_valor_dos_servicos():
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT AVG(valor) AS media_valor_servicos
    FROM Servico;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def listar_veiculos_atendidos_por_mes(ano, mes):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT DISTINCT v.id_veiculo, v.marca, v.modelo, v.ano, v.placa
    FROM Veiculo v
    JOIN Cliente c ON v.id_cliente = c.id_cliente
    JOIN Fatura f ON c.id_cliente = f.id_cliente
    WHERE YEAR(f.data) = %s AND MONTH(f.data) = %s;
    """
    cursor.execute(query, (ano, mes))
    result = cursor.fetchall()
    conn.close()
    return result

def listar_total_caixa_por_periodo(data_inicio, data_fim):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT SUM(valor_total) AS total_caixa
    FROM Fatura
    WHERE data BETWEEN %s AND %s;
    """
    cursor.execute(query, (data_inicio, data_fim))
    result = cursor.fetchone()
    conn.close()
    return result

def listar_dados_de_fatura(id_fatura):
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT f.id_fatura, f.data, f.valor_total, c.nome AS cliente, c.telefone, c.email
    FROM Fatura f
    JOIN Cliente c ON f.id_cliente = c.id_cliente
    WHERE f.id_fatura = %s;
    """
    cursor.execute(query, (id_fatura,))
    result = cursor.fetchone()
    conn.close()
    return result

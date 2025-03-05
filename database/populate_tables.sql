-- Inserção de Clientes
INSERT INTO Cliente (nome, telefone, email) VALUES
('João Silva', '1234-5678', 'joao.silva@email.com'),
('Maria Oliveira', '8765-4321', 'maria.oliveira@email.com'),
('Carlos Souza', '5555-5555', 'carlos.souza@email.com'),
('Ana Costa', '1111-2222', 'ana.costa@email.com'),
('Pedro Rocha', '3333-4444', 'pedro.rocha@email.com'),
('Lucia Lima', '6666-7777', 'lucia.lima@email.com'),
('Fernando Santos', '8888-9999', 'fernando.santos@email.com'),
('Juliana Pereira', '2222-3333', 'juliana.pereira@email.com'),
('Ricardo Almeida', '4444-5555', 'ricardo.almeida@email.com'),
('Camila Gonçalves', '7777-8888', 'camila.goncalves@email.com');

-- Inserção de Veículos
INSERT INTO Veiculo (id_cliente, marca, modelo, ano, placa) VALUES
(1, 'Toyota', 'Corolla', 2018, 'ABC-1234'),
(2, 'Honda', 'Civic', 2019, 'DEF-5678'),
(3, 'Ford', 'Focus', 2017, 'GHI-9101'),
(4, 'Chevrolet', 'Onix', 2020, 'JKL-1121'),
(5, 'Volkswagen', 'Golf', 2016, 'MNO-3141'),
(6, 'Fiat', 'Uno', 2015, 'PQR-5161'),
(7, 'Renault', 'Sandero', 2019, 'STU-7181'),
(8, 'Hyundai', 'HB20', 2021, 'VWX-9202'),
(9, 'Nissan', 'Versa', 2018, 'YZA-1222'),
(10, 'Kia', 'Cerato', 2020, 'BCD-3242');

-- Inserção de Serviços
INSERT INTO Servico (descricao, valor) VALUES
('Troca de Óleo', 100.00),
('Alinhamento', 80.00),
('Balanceamento', 70.00),
('Revisão Geral', 200.00),
('Troca de Pneus', 300.00),
('Troca de Pastilhas de Freio', 150.00),
('Troca de Bateria', 250.00),
('Reparo no Motor', 500.00),
('Troca de Amortecedores', 400.00),
('Limpeza do Sistema de Ar Condicionado', 120.00);

-- Inserção de Funcionários
INSERT INTO Funcionario (nome, funcao, telefone) VALUES
('José Alves', 'Mecânico', '1111-1111'),
('Antonio Carlos', 'Eletricista', '2222-2222'),
('Marcos Paulo', 'Mecânico', '3333-3333'),
('Luiz Fernando', 'Atendente', '4444-4444'),
('Carlos Eduardo', 'Mecânico', '5555-5555'),
('Fernanda Lima', 'Eletricista', '6666-6666'),
('Patricia Souza', 'Atendente', '7777-7777'),
('Roberto Almeida', 'Mecânico', '8888-8888'),
('Sandra Gomes', 'Eletricista', '9999-9999'),
('Ricardo Oliveira', 'Atendente', '0000-0000');

-- Inserção de Faturas
INSERT INTO Fatura (id_cliente, data, valor_total) VALUES
(1, '2023-10-01', 180.00),
(2, '2023-10-02', 150.00),
(3, '2023-10-03', 300.00),
(4, '2023-10-04', 250.00),
(5, '2023-10-05', 400.00),
(6, '2023-10-06', 120.00),
(7, '2023-10-07', 500.00),
(8, '2023-10-08', 200.00),
(9, '2023-10-09', 350.00),
(10, '2023-10-10', 280.00);

-- Inserção de Serviços nas Faturas
INSERT INTO Servico_Fatura (id_servico, id_fatura) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(6, 5),
(7, 6),
(8, 7),
(9, 8),
(10, 9);
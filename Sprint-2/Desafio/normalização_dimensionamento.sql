-- ========= NORMALIZAÇÃO ========= --

-- Tabela cliente
CREATE TABLE cliente (
   idCliente INT PRIMARY KEY,
   nomeCliente VARCHAR(255),
   cidadeCliente VARCHAR(255),
   estadoCliente VARCHAR(255),
   paisCliente VARCHAR(255)
)
-- Tabela vendedor
CREATE TABLE vendedor (
   idVendedor INT PRIMARY KEY,
   nomeVendedor VARCHAR(255),
   sexoVendedor BOOLEAN,
   estadoVendedor VARCHAR(255)
)
-- Tabela carro
CREATE TABLE carro (
   idCarro INT PRIMARY KEY,
   kmCarro FLOAT,
   classiCarro VARCHAR(255),
   marcaCarro VARCHAR(255),
   modeloCarro VARCHAR(255),
   anoCarro FLOAT,
   idCombustivel INT,
   tipoCombustivel VARCHAR(255)
)

-- Tabela locacao
CREATE TABLE locacao (
   idLocacao INT PRIMARY KEY,
   idCarro INT,
   idCliente INT,
   idVendedor INT,
   dataLocacao DATE,
   horaLocacao TIME,
   qtdDiaria INT,
   vlrDiaria FLOAT,
   dataEntrega DATE,
   horaEntrega TIME,
   FOREIGN KEY (idCarro) REFERENCES carro(idCarro),
   FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),
   FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor)
)

-- Inserir dados tabela cliente
INSERT INTO cliente(idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao

-- Inserir dados tabela vendedor (converter boolean pra char)
INSERT INTO vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

-- Inserir dados tabela carro (está com erro)
INSERT INTO carro(idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel)
SELECT DISTINCT idLocacao, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel
from tb_locacao

-- Inserir dados tabela locacao
INSERT INTO locacao(idLocacao, idCarro, idCliente, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCarro, idCliente, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao

-- Modelo relacional --
SELECT * FROM cliente  cl
SELECT * FROM vendedor ve
SELECT * FROM carro    ca
SELECT * FROM locacao lo
SELECT * FROM tb_locacao

-- Atualizar formato de data das colunas dataLocacao e dataEntrega da tabela locacao (relacional)
UPDATE locacao SET
dataLocacao = substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao, 7, 2),
dataEntrega = substr(dataEntrega, 1, 4) || '-' || substr(dataEntrega, 5, 2) || '-' || substr(dataEntrega, 7, 2)
WHERE dataLocacao IS NOT NULL
AND dataEntrega IS NOT NULL

-- ========= Modelo dimensional ========= --

CREATE TABLE dim_cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(255),
    cidadeCliente VARCHAR(255),
    estadoCliente VARCHAR(255),
    paisCliente VARCHAR(255)
)

CREATE TABLE dim_vendedor (
   idVendedor INT PRIMARY KEY,
   nomeVendedor VARCHAR(255),
   sexoVendedor BOOLEAN,
   estadoVendedor VARCHAR(255)
)

CREATE TABLE dim_carro (
   idCarro INT PRIMARY KEY,
   kmCarro FLOAT,
   classiCarro VARCHAR(255),
   marcaCarro VARCHAR(255),
   modeloCarro VARCHAR(255),
   anoCarro FLOAT,
   idCombustivel INT,
   tipoCombustivel VARCHAR(255)
)

CREATE TABLE dim_data (
  idData INT PRIMARY KEY,
  dataLocacao DATE,
  horaLocacao TIME,
  dataEntrega DATE,
  horaEntrega TIME
)

CREATE TABLE fato_locacao (
  idLocacao INT PRIMARY KEY,
  idCarro INT,
  idCliente INT,
  idVendedor INT,
  idData INT,
  dataLocacao DATE,
  horaLocacao TIME,
  qtdDiaria INT,
  vlrDiaria FLOAT,
  dataEntrega DATE,
  horaEntrega TIME,
  FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
  FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
  FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor),
  FOREIGN KEY (idData) REFERENCES dim_data(idData)
)

-- Modelo dimensional --
SELECT * FROM dim_carro
SELECT * FROM dim_cliente
SELECT * FROM dim_vendedor
SELECT * FROM dim_data
SELECT * FROM fato_locacao

-- Populando a tabela dimensional --
INSERT INTO dim_cliente(idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM cliente

INSERT INTO dim_vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM vendedor

INSERT INTO dim_carro(idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel, tipoCombustivel
FROM carro

INSERT INTO dim_data(idData, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega
FROM locacao

INSERT INTO fato_locacao(idLocacao, idCarro, idCliente, idVendedor, idData, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, idCarro, idCliente, idVendedor, idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM locacao


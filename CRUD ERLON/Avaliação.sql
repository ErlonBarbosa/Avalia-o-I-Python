create database je_veiculos;
use je_veiculos;

CREATE TABLE veiculos (
    vei_id INT AUTO_INCREMENT PRIMARY KEY,
    vei_tipo VARCHAR(255),
    vei_cor VARCHAR(255),
    vei_modelo VARCHAR(255),
    vei_marca varchar(255),
    vei_ano INT,
    vei_estado VARCHAR(255),
    vei_km_rodados INT,
    vei_leilao VARCHAR(10),
    vei_formas_pagamento VARCHAR(255)
);

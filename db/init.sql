-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS langapp;

-- Seleciona o banco de dados
USE langapp;

-- Tabela Concept
CREATE TABLE IF NOT EXISTS concept (
    id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    description VARCHAR(255),
    type VARCHAR(50)
);

-- Tabela Language
CREATE TABLE IF NOT EXISTS languages (
    id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    hasCourse BOOLEAN
);

-- Tabela User
CREATE TABLE IF NOT EXISTS user (
    id INT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    sourceLanguage_id INT,
    targetLanguage_id INT,
    FOREIGN KEY (sourceLanguage_id) REFERENCES languages(id),
    FOREIGN KEY (targetLanguage_id) REFERENCES languages(id)
);

-- Tabela Card
CREATE TABLE IF NOT EXISTS cards  (
    id INT PRIMARY KEY,
    hasAudio BOOLEAN,
    front VARCHAR(255),
    verse VARCHAR(255),
    sourceLanguage_id INT,
    targetLanguage_id INT,
    creator_id INT,
    FOREIGN KEY (sourceLanguage_id) REFERENCES languages(id),
    FOREIGN KEY (targetLanguage_id) REFERENCES languages(id),
    FOREIGN KEY (creator_id) REFERENCES user(id)
);


-- Tabela Card_Concept
CREATE TABLE IF NOT EXISTS card_concept (
    card_id INT,
    concept_id INT,
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (concept_id) REFERENCES concept(id),
	PRIMARY KEY (card_id, concept_id)
);


-- Tabela User_Concept
CREATE TABLE IF NOT EXISTS user_concept (
    user_id INT,
    concept_id INT,
    retentionConstant FLOAT,
    review_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (concept_id) REFERENCES concept(id),
    PRIMARY KEY (user_id, concept_id)
);

-- Tabela Comment
CREATE TABLE IF NOT EXISTS comment (
    id INT PRIMARY KEY,
    text VARCHAR(255),
    created_at DATETIME,
    card_id INT,
    creator_id INT,
    replyTo_id INT,
    FOREIGN KEY (card_id) REFERENCES cards(id),
    FOREIGN KEY (creator_id) REFERENCES user(id),
    FOREIGN KEY (replyTo_id) REFERENCES comment(id)
);

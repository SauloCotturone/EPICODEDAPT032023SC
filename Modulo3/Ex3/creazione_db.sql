CREATE DATABASE Epicode_Dapt;

USE Epicode_Dapt;

CREATE TABLE Store(
	ID_Store INT PRIMARY KEY,
	Indirizzo VARCHAR(255) NOT NULL,
	Nr_telefono VARCHAR(15)
);

CREATE TABLE Settore(
	ID_Settore INT,
	ID_Store INT,
	PRIMARY KEY(ID_Settore, ID_Store),
    FOREIGN KEY(ID_Store) REFERENCES Store(ID_Store) ON UPDATE CASCADE ON DELETE NO ACTION
);

CREATE TABLE Impiegato(
	ID_Impgt VARCHAR(255) PRIMARY KEY,
    ID_Store INT,
    Nome VARCHAR(255),
    Titolo_studio VARCHAR(255),
    Recapito VARCHAR(255),
    FOREIGN KEY (ID_Store) REFERENCES Store(ID_Store) ON UPDATE CASCADE ON DELETE NO ACTION
);

ALTER TABLE Impiegato
CHANGE ID_Impgt CF VARCHAR(255);

CREATE TABLE Videogioco(
Titolo VARCHAR(255),
Sviluppatore VARCHAR(255),

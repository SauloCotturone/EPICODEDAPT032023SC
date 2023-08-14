CREATE DATABASE Aeroporti_ex4_M3;

USE Aeroporti_ex4_M3;

CREATE TABLE Aeroporto(
	Città VARCHAR(255),
	Nazione VARCHAR(255),
	NumPiste VARCHAR(255)
);

CREATE TABLE Volo(
ID_Volo INT,
GiornoSett VARCHAR(255),
CittàPart VARCHAR(255),
OraPart VARCHAR(255),
CittàArr VARCHAR(255),
OraArr DATETIME,
TipoAereo VARCHAR(255)
);

CREATE TABLE Aereo(
TipoAereo VARCHAR(255),
NumPasseggeri INT,
QtaMerci INT
);

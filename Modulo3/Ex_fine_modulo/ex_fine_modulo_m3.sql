CREATE DATABASE ex_finale_m3;

USE ex_finale_m3;

CREATE TABLE Giocatore(
	CF_giocatore VARCHAR(16) PRIMARY KEY,
    Nome VARCHAR(100),
    Ruolo VARCHAR(100),
    Età INT UNSIGNED
);

ALTER TABLE Giocatore ADD Squadra VARCHAR(100);
ALTER TABLE Giocatore ADD FOREIGN KEY (Squadra) REFERENCES Squadra(Nome_squadra)
ON UPDATE CASCADE ON DELETE NO ACTION;


CREATE TABLE Squadra(
	Nome_squadra VARCHAR(100) PRIMARY KEY,
    Stadio VARCHAR(100),
    Anno_fondazione YEAR,
    Città VARCHAR(100)
);

ALTER TABLE Squadra ADD Titoli_vinti VARCHAR(100);
CREATE INDEX idx_Stadio ON Squadra(Stadio);

CREATE TABLE Partita(
	Id_partita INT PRIMARY KEY AUTO_INCREMENT,
	Squadra_casa VARCHAR(100),
    Squadra_ospite VARCHAR(100),
    Data_evento DATETIME,
    Risultato VARCHAR(100),
    Rigori INT,
    Ammonizioni INT,
    Punizioni INT,
    Corner INT,
    Tiri_in_porta INT,
		FOREIGN KEY (Squadra_casa) REFERENCES Squadra(Nome_squadra) 
        ON UPDATE CASCADE ON DELETE NO ACTION,
        FOREIGN KEY (Squadra_ospite) REFERENCES Squadra(Nome_squadra) 
        ON UPDATE CASCADE ON DELETE NO ACTION
);

ALTER TABLE Partita ADD Arbitro_designato VARCHAR(100);
ALTER TABLE Partita ADD Stadio VARCHAR(100);
ALTER TABLE Partita ADD FOREIGN KEY(Arbitro_designato) REFERENCES Arbitro(Nome_arbitro) 
ON UPDATE CASCADE ON DELETE NO ACTION;
ALTER TABLE Partita ADD FOREIGN KEY(Stadio) REFERENCES Squadra(Stadio) 
ON UPDATE CASCADE ON DELETE NO ACTION;

CREATE TABLE Allenatore (
    Nome_allenatore VARCHAR(100) PRIMARY KEY,
    Titoli_vinti VARCHAR(100),
    Squadra_appartenenza VARCHAR(100),
    Anno_inizio_contratto YEAR,
    Anno_fine_contratto YEAR
);

ALTER TABLE Allenatore ADD FOREIGN KEY(Squadra_appartenenza) REFERENCES Squadra(Nome_squadra)
ON UPDATE CASCADE ON DELETE NO ACTION;

CREATE TABLE Arbitro (
	Nome_arbitro VARCHAR(100) PRIMARY KEY,
    Anno_inizio_carriera YEAR
);

ALTER TABLE Arbitro ADD Sezione VARCHAR(100);


### QUERIES ESPLORATIVE
SELECT Nome_squadra
FROM Squadra;

SELECT COUNT(Nome)
FROM Giocatore;

SELECT Nome
FROM Giocatore
WHERE Squadra = "Milan";


### 10 INTERROGAZIONI SUL DATABASE
##1 ELENCO GIOCATORI DI UNA SQUADRA CON ETA’ SUPERIORE AI 30 ANNI
SELECT Nome, Età
FROM Giocatore AS G
WHERE Squadra = "Milan" AND G.Età > 30
ORDER BY G.Età DESC;


##2 ORDINE DELLE SQUADRE PER ETA’ MEDIA PIU’ BASSA
SELECT Squadra, AVG(Età) AS Età_media
FROM Giocatore AS G
GROUP BY Squadra
ORDER BY Età_media ASC;


##3 L’ARBITRO CHE HA ARBITRATO PIU’ PARTITE NEL 2023
SELECT Arbitro_designato, COUNT(Arbitro_designato) AS Range_arbitri
from Partita
WHERE YEAR(Data_evento) = 2023
GROUP BY Arbitro_designato
ORDER BY Range_arbitri DESC;


##4 NUMERO DI ARBITRI PER SEZIONE
SELECT Sezione, COUNT(*) AS Numero_arbitri
FROM Arbitro
GROUP BY Sezione;


##5 NUMERO DI PARTITE GIOCATE DAL MILAN IN CASA NEL 2023
SELECT Squadra_casa AS Team, COUNT(*) AS Numero_partite_giocate
FROM Partita
WHERE Squadra_casa = "Milan" AND YEAR(Data_evento) = 2023
GROUP BY Team
ORDER BY Numero_partite_giocate DESC;


##6 ALLENATORI ANCORA IN CARICA PER SINGOLA SQUADRA
SELECT Nome_allenatore, Nome_squadra
FROM Allenatore AS A
JOIN Squadra AS S ON A.Squadra_appartenenza = S.Nome_squadra
WHERE A.Anno_fine_contratto IS NULL;


##7 ELENCARE IL PIU’ ALTO NUMERO DI RIGORI CONCESSI PER SQUADRA IN CASA E L’ARBITRO CHE LI HA CONCESSI;
SELECT SQ.Squadra_casa, SQ.Max_rigori, A.Nome_arbitro
FROM
	(SELECT Squadra_casa, MAX(Rigori) AS Max_rigori
    FROM Partita
    GROUP BY Squadra_casa
) AS SQ
JOIN PARTITA AS P ON P.Squadra_casa =SQ.Squadra_casa AND P.Rigori = SQ.Max_rigori
JOIN Arbitro AS A ON P.Arbitro_designato = A.Nome_arbitro;


##8 IL RISULTATO NEL DERBY TRA MILNA E INTER DISPUTATO NEL 2022 DI MATTINA, CON INDICAZIONE DEL NUMERO DI TIRI E DELL’ARBITRO DESIGNATO 
SELECT Risultato, Squadra_casa, Tiri_in_porta, Arbitro_designato
FROM Partita
WHERE TIME(Data_evento) BETWEEN "08:00:00" AND "13:00:00"
AND YEAR(Data_evento) = 2022
AND Squadra_casa IN ('Inter', 'Milan')
AND Squadra_ospite IN ('Inter', 'Milan');


##9 I DUE MATCH RISPETTIVAMENTE DEL 2022 E DEL 2023 CHE HANNO VISO ASSEGNARE IL PIU' ALTO NUMERO DI RIGORI CON INFO SULL'ARBITRO CHE HA SOPRASSEDUTO 
(SELECT *
FROM Partita AS P
JOIN Arbitro AS A ON P.Arbitro_designato = A.Nome_arbitro
WHERE YEAR(Data_evento) = 2022
ORDER BY Rigori DESC
Limit 1)
UNION ALL
(SELECT *
FROM Partita AS P
JOIN Arbitro AS A ON P.Arbitro_designato = A.Nome_arbitro
WHERE YEAR(Data_evento) = 2023
ORDER BY Rigori DESC
Limit 1);


##10 GIOCATORE PIU' GIOVANE PER SQUADRA
SELECT S.Nome_squadra, G.Nome AS Nome_giocatore, G.Età AS Età_minima
FROM (
    SELECT Squadra, MIN(Età) AS Età_minima
    FROM Giocatore
    GROUP BY Squadra
) AS Min_età_per_squadra
JOIN Giocatore AS G ON Min_età_per_squadra.Squadra = G.Squadra AND Min_età_per_squadra.Età_minima = G.Età
JOIN Squadra AS S ON G.Squadra = S.Nome_squadra;

 
    
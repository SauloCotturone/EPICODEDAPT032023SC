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

SHOW COLUMNS FROM Impiegato;

CREATE TABLE Videogioco(
Titolo VARCHAR(255),
Sviluppatore VARCHAR(255),
Anno_distribuzione YEAR,
Genere VARCHAR(255),
Prezzo DOUBLE,
Remake BOOLEAN,
	PRIMARY KEY(Titolo, Sviluppatore)
);

ALTER TABLE Videogioco
ADD CONSTRAINT PRIMARY KEY(Titolo, Sviluppatore);

CREATE INDEX IDX_titolo ON Videogioco(Titolo);
CREATE INDEX IDX_sviluppatore ON Videogioco(Sviluppatore);

CREATE TABLE Si_trova_in(
ID_Store INT,
ID_Settore INT,
Titolo VARCHAR(255),
Sviluppatore VARCHAR(255),
Disponibilità BOOLEAN,
Posizione VARCHAR(255),
	PRIMARY KEY(ID_Store, ID_Settore, Titolo, Sviluppatore),
	FOREIGN KEY(ID_Store) REFERENCES Store(ID_Store) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY(ID_Settore) REFERENCES Settore(ID_Settore) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY(Titolo) REFERENCES Videogioco(Titolo) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY(Sviluppatore) REFERENCES Videogioco(Sviluppatore) ON UPDATE CASCADE ON DELETE NO ACTION
    );


SHOW COLUMNS FROM Videogioco;

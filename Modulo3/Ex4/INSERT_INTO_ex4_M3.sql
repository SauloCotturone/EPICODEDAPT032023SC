USE aeroporti_ex4_m3;

INSERT INTO Aeroporto(
	Città, Nazione, NumPiste)
VALUES(
		"Roma", "Italia", 3),
		("Milano","Italia", 2),
		("Napoli","Italia", 2),
		("Torino","Italia", 1),
		("Venezia","Italia", NULL),
		("Bologna","Italia", 3),
		("Firenze","Italia", 2),
		("Palermo","Italia", 2),
		("Catania","Italia", 1),
		("Genova","Italia", 1),
		("Bari","Italia", NULL),
		("Verona","Italia", 1),
		("Cagliari","Italia", 1),
		("Pisa","Italia", 2),
		("Turin", "Italia", 3);

UPDATE Aeroporto SET NumPiste = NULL WHERE Città = "Venezia";
UPDATE Aeroporto SET NumPiste = NULL WHERE Città = "Bari";

SELECT * FROM Aeroporto;

INSERT INTO Volo(
	ID_Volo, GiornoSett, CittàPart, OraPart, CittàArr, OraArr, TipoAereo)
VALUES(
	'AZ100', 'MAR', "Torino", '10:00', "Bari", '11:00', 'Boeing_777'),
	('YB456', "GIO", "Roma", '12:00', "Venezia", '13:00', 'Boeing_737'),
	('KF789', "DOM", "Bologna", '14:50', "Palermo", '15:55', 'Airbus_A330'),
	('LM234', "VEN", "Verona", '16:15', "Roma", '17:15', 'Airbus_A350'),
	('QP567', "MAR", "Firenze", '18:00', "Cagliari", '19:00', 'Boeing_737'),
	('AZ274', "LUN", "Napoli", '06:00', "Milano", '07:00', 'Airbus_A330'),
	('TR123', "VEN", "Cagliari", '09:30', "Torino", '10:30', 'Airbus_A320'),
	('VD678', "MER", "Venezia", '10:30', "Genova", '11:30', 'Airbus_A350'),
	('OI345', "MER", "Milano", '12:00', "Napoli", '13:00', 'Boeing_777'),
	('HW678', "GIO", "Bari", '19:00', "Bologna", '20:00', 'Airbus_A320');
    
SELECT DISTINCT TipoAereo FROM Volo;
    
INSERT INTO Aereo(
	TipoAereo, NumPasseggeri, QtaMerci)
VALUES(
	'Boeing_777', 180, 5000),
    ('Airbus_A330', 120, 2400),
    ('Airbus_A320', 130, 3000),
    ('Airbus_A350', 140, 3800),
    ('Boeing_737', 160, 4600);

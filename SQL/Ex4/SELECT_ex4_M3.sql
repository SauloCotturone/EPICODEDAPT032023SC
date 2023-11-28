SELECT Città FROM Aeroporto WHERE NumPiste IS NULL;

SELECT TipoAereo FROM Volo WHERE CittàPart = "Torino";

SELECT CittàPart FROM Volo WHERE CittàArr = "Bologna";

SELECT CittàPart, CittàArr FROM Volo WHERE ID_Volo = "AZ274";

SELECT TipoAereo, GiornoSett, OraPart FROM Volo 
WHERE CittàPart LIKE "B%" AND CittàArr LIKE "%E%A";
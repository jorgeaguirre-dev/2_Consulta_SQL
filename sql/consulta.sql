SELECT A.nombrePersona1 AS nombrePersona, M2.nombreGrupo
FROM Amigo A
JOIN Miembro M2 ON A.nombrePersona2 = M2.nombrePersona -- Amigos que están en grupos
WHERE NOT EXISTS (
    -- 1. Validar que la persona NO sea miembro de ese grupo
    SELECT 1 FROM Miembro M1
    WHERE M1.nombrePersona = A.nombrePersona1
      AND M1.nombreGrupo = M2.nombreGrupo
)
GROUP BY A.nombrePersona1, M2.nombreGrupo
HAVING COUNT(DISTINCT A.nombrePersona2) = (
    -- 2. Validar que la cantidad de amigos en ese grupo
    -- sea igual al total de amigos que tiene la persona
    SELECT COUNT(*) FROM Amigo A2
    WHERE A2.nombrePersona1 = A.nombrePersona1
);
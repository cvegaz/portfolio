-- This SQL query retrieves information about players who have the fastest 40-yard dash times for their respective positions.
SELECT dp.matricula, dp.first_name, dp.last_name_paternal, dp.position, pt.yds_40_1, pt.test_date
FROM data_player dp
JOIN physical_test pt ON dp.matricula = pt.matricula
WHERE pt.yds_40_1 IS NOT NULL AND pt.yds_40_1 != 0
AND pt.yds_40_1 = (
    SELECT MIN(pt2.yds_40_1)
    FROM physical_test pt2
    JOIN data_player dp2 ON dp2.matricula = pt2.matricula
    WHERE dp2.position = dp.position
    AND pt2.yds_40_1 IS NOT NULL AND pt2.yds_40_1 != 0
)


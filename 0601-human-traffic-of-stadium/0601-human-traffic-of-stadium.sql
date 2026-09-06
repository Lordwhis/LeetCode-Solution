WITH valid AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
qualified_groups AS (
    SELECT grp
    FROM valid
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT
    v.id,
    v.visit_date,
    v.people
FROM valid v
JOIN qualified_groups q
    ON v.grp = q.grp
ORDER BY v.visit_date;

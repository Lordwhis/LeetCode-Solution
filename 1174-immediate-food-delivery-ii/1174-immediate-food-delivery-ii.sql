WITH first_order AS (    
    SELECT
        customer_id,
        MIN(order_date) AS orderD,
        MIN(customer_pref_delivery_date) AS deliD
    FROM delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(
        AVG(
            CASE
                WHEN f.orderD = f.deliD THEN 1
                ELSE 0
            END
        ) * 100,
        2
    ) AS immediate_percentage
FROM first_order f;
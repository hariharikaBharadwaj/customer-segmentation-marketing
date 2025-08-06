-- STEP 3: Create stored procedures

DELIMITER //

CREATE PROCEDURE GetSubscriptionByEducation()
BEGIN
    SELECT 
        education,
        COUNT(*) AS total,
        SUM(y) AS subscribed
    FROM bank_data
    GROUP BY education;
END //

CREATE PROCEDURE GetAvgBalanceByJob()
BEGIN
    SELECT 
        job,
        AVG(balance) AS avg_balance
    FROM bank_data
    GROUP BY job;
END //

CREATE PROCEDURE GetSubscriptionByAgeGroup()
BEGIN
    SELECT 
        CASE 
            WHEN age < 25 THEN 'Under 25'
            WHEN age BETWEEN 25 AND 34 THEN '25–34'
            WHEN age BETWEEN 35 AND 44 THEN '35–44'
            WHEN age BETWEEN 45 AND 54 THEN '45–54'
            WHEN age BETWEEN 55 AND 64 THEN '55–64'
            ELSE '65+'
        END AS age_group,
        COUNT(*) AS total_customers,
        SUM(y) AS total_subscribed,
        ROUND(SUM(y) / COUNT(*) * 100, 2) AS subscription_rate_pct
    FROM bank_data
    GROUP BY age_group
    ORDER BY FIELD(age_group, 'Under 25', '25–34', '35–44', '45–54', '55–64', '65+');
END //

DELIMITER ;


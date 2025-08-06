


-- STEP 1: Create database and clean table
CREATE DATABASE IF NOT EXISTS bank_marketing_cleandata;
USE bank_marketing_cleandata;

DROP TABLE IF EXISTS bank_data;

CREATE TABLE bank_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    job VARCHAR(50),
    marital VARCHAR(20),
    education VARCHAR(50),
    balance INT,
    default_status INT,
    housing INT,
    loan INT,
    contact VARCHAR(20),
    month VARCHAR(20),
    duration INT,
    campaign INT,
    pdays INT,
    previous INT,
    poutcome VARCHAR(20),
    y INT
);

-- STEP 2: Drop existing stored procedures if they exist
DROP PROCEDURE IF EXISTS GetSubscriptionByEducation;
DROP PROCEDURE IF EXISTS GetAvgBalanceByJob;
DROP PROCEDURE IF EXISTS GetSubscriptionByAgeGroup;


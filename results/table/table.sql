
    \sql
    \connect root@localhost
    DROP DATABASE IF EXISTS db;
    CREATE DATABASE IF NOT EXISTS db;
    USE db;
    
    CREATE TABLE IF NOT EXISTS file1 (
    	ï»¿Ã¯Â»Â¿"FACTSET_PERSON_ID" VARCHAR(300),
	PEOPLE_NAME_TYPE VARCHAR(300),
	PEOPLE_NAME_VALUE VARCHAR(300)
    )
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_unicode_ci';
        
        LOAD DATA INFILE 'c:/Python/edgar/resources/table/encoding/file1.txt' REPLACE INTO TABLE file1
        CHARACTER SET 'utf8mb4'
        FIELDS TERMINATED BY '|' ENCLOSED BY '"' ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n' STARTING BY ''
        IGNORE 1 LINES;
        
    CREATE TABLE IF NOT EXISTS file2 (
    	ï»¿Ã¯Â»Â¿"FACTSET_PERSON_ID" VARCHAR(300),
	PEOPLE_NAME_TYPE VARCHAR(300),
	PEOPLE_NAME_VALUE VARCHAR(300)
    )
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_unicode_ci';
        
        LOAD DATA INFILE 'c:/Python/edgar/resources/table/encoding/file2.txt' REPLACE INTO TABLE file2
        CHARACTER SET 'utf8mb4'
        FIELDS TERMINATED BY '|' ENCLOSED BY '"' ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n' STARTING BY ''
        IGNORE 1 LINES;
        
    CREATE TABLE IF NOT EXISTS ppl_names (
    	ï»¿"FACTSET_PERSON_ID" VARCHAR(300),
	PEOPLE_NAME_TYPE VARCHAR(300),
	PEOPLE_NAME_VALUE VARCHAR(300)
    )
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_unicode_ci';
        
        LOAD DATA INFILE 'c:/Python/edgar/resources/table/encoding/ppl_names.txt' REPLACE INTO TABLE ppl_names
        CHARACTER SET 'utf8mb4'
        FIELDS TERMINATED BY '|' ENCLOSED BY '"' ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n' STARTING BY ''
        IGNORE 1 LINES;
        
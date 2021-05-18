
\sql
\connect root@localhost
DROP DATABASE IF EXISTS db;
CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS edgarSubmission (
	accession VARCHAR(300),
	schemaVersion VARCHAR(300),
	submissionType VARCHAR(300),
	cik VARCHAR(300),
	entityName VARCHAR(300),
	street1 VARCHAR(300),
	issuerPhoneNumber VARCHAR(300),
	jurisdictionOfInc VARCHAR(300)
)
CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_unicode_ci';
    
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-000058.txt' REPLACE INTO TABLE edgarSubmission
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<edgarSubmission>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-000511.txt' REPLACE INTO TABLE edgarSubmission
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<edgarSubmission>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-001268.txt' REPLACE INTO TABLE edgarSubmission
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<edgarSubmission>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-001881.txt' REPLACE INTO TABLE edgarSubmission
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<edgarSubmission>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-003897.txt' REPLACE INTO TABLE edgarSubmission
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<edgarSubmission>';
        
CREATE TABLE IF NOT EXISTS relatedPersonInfo (
	accession VARCHAR(300),
	firstName VARCHAR(300),
	lastName VARCHAR(300),
	street1 VARCHAR(300),
	street2 VARCHAR(300),
	city VARCHAR(300),
	stateOrCountry VARCHAR(300),
	stateOrCountryDescription VARCHAR(300),
	zipCode VARCHAR(300)
)
CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_unicode_ci';
    
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-000058.txt' REPLACE INTO TABLE relatedPersonInfo
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<relatedPersonInfo>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-000511.txt' REPLACE INTO TABLE relatedPersonInfo
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<relatedPersonInfo>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-001268.txt' REPLACE INTO TABLE relatedPersonInfo
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<relatedPersonInfo>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-001881.txt' REPLACE INTO TABLE relatedPersonInfo
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<relatedPersonInfo>';
        
    LOAD XML INFILE 'C:/Python/edgar/resources/xml/clean/1000275_0001214659-13-003897.txt' REPLACE INTO TABLE relatedPersonInfo
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<relatedPersonInfo>';
        
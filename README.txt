*INSTALL REQUIREMENTS
pip install -r requirements.txt


--------------------------------------------------------------------------------------------
*STUDY MATERIALS - WRDS SEC ANALYTICS SUITE
https://wrds-www.wharton.upenn.edu/pages/get-data/wrds-sec-analytics-suite/

*STUDY MATERIALS - SEC - DATA
https://www.sec.gov/sec-data-resources
https://www.sec.gov/dera/data
https://www.sec.gov/info/edgar/siccodes.htm
https://www.sec.gov/search/search.htm (FULL TEXT SEARCH)

*STUDY MATERIALS - SEC - DIVISIONS & OFFICES
https://www.sec.gov/divisions.shtml
https://www.sec.gov/page/corpfin-section-landing
https://www.sec.gov/page/enforcement-section-landing
https://www.sec.gov/investment-management
https://www.sec.gov/dera
https://www.sec.gov/divisions/trading-markets

*STUDY MATERIALS - SEC - ENFORCEMENT
https://www.sec.gov/page/litigation
https://www.sec.gov/litigations/sec-action-look-up

*STUDY MATERIALS - SEC - REGULATION
https://www.sec.gov/page/regulation
https://www.investor.gov/introduction-investing/investing-basics/role-sec/laws-govern-securities-industry
https://www.investor.gov/introduction-investing/investing-basics/role-sec/researching-federal-securities-laws-through-sec

*STUDY MATERIALS - SEC - EDUCATION
https://www.investor.gov/
https://www.investor.gov/introduction-investing/getting-started/researching-investments
https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work
https://www.investor.gov/introduction-investing/investing-basics/glossary

*STUDY MATERIALS - SEC - FILINGS
https://www.sec.gov/edgar.shtml
https://www.sec.gov/forms
https://www.sec.gov/info/edgar/forms/edgform.pdf
https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual
https://www.sec.gov/structureddata/osd-inline-xbrl.html
http://xbrlview.fasb.org/yeti/resources/yeti-gwt/Yeti.jsp
https://github.com/TiesdeKok/xbrl-api-playground

*STUDY MATERIALS - SEC - FINRA
https://www.finra.org/#/
https://www.finra.org/investors/tools-and-calculators
http://finra-markets.morningstar.com/MarketData/
https://tools.finra.org/fund_analyzer/


------------------OLD------------------
*PRELIMINARY
fill "resources/varlist.csv"

*CREATE DATABASES
py main.py -a

*CREATE DO FILES AND VARIABLE NAMES
py main.py -b
------------------OLD------------------


--------------------------------------------------------------------------------------------
*FUNCTIONS:
*DOWNLOAD TXT (with FINAL REPORT)
fill "resources/txt/txt.dta", read column "fname" (from "WRDS SEC Analytics Suite - SEC Filings on WRDS" https://wrds-web.wharton.upenn.edu/wrds//ds/sec/wforms/filings.cfm)
py main.py -txt

*FROM HTML TO TXT
fill "resources/html/"
py main.py -html

*FROM (DELIMITER-SEPARATED) TABLE TO SQL
fill "resources/table/files/"
set delimiter (e.g., "," or "|" or "tab")
py main.py -table "|"

*FROM XML TO SQL
fill "resources/xml/files/"
fill "resources/xml/schema.csv"
py main.py -xml


--------------------------------------------------------------------------------------------
*SEE RESULTS
see "results/"


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*SETUP
*MYSQL - FIRST TIME
install MySQL ("Windows (x86, 32-bit), MSI Installer" from https://dev.mysql.com/downloads/installer/)
go to "C:\ProgramData\MySQL\MySQL Server 8.0\my.ini"-> find (Ctrl+F) "secure-file-priv" -> write ' secure-file-priv="" '
press "Windows Key" -> search "Services" -> search "MySQL80" -> Right-click -> select "Start"
open "C:\Program Files\MySQL\MySQL Shell 8.0\bin\mysqlsh.exe" (MySQL Shell)
\sql
\connect root@localhost
SET NAMES 'utf8mb4';
SET CHARACTER SET 'utf8mb4';
CREATE DATABASE db;
USE db;
SHOW TABLES;

*ODBC SERVER - FIRST TIME
press "Windows Key" -> search "ODBC Data Sources" -> select "User DSN" -> select "Add" -> select "MySQL Unicode 8.0 Driver " -> select "Finish" 
Data Source Name:"data source"
Description:"data source"
TCP/IP Server:"127.0.0.1"; Port:"3306"
User:"root"
Password:"123456"
Database:"db"
select "Test"; select "OK"; select "OK"


--------------------------------------------------------------------------------------------
*FROM (DELIMITER-SEPARATED) TABLE TO SQL (https://dev.mysql.com/doc/refman/8.0/en/load-data.html)
press "Windows Key" -> search "Services" -> search "MySQL80" -> Right-click -> select "Start"
open "C:\Program Files\MySQL\MySQL Shell 8.0\bin\mysqlsh.exe" (MySQL Shell)
\sql
\connect root@localhost 
USE db;
SHOW TABLES; 
DROP TABLE table; (OPTIONAL)
SOURCE "C:/Python/edgar/results/table/table.sql";


--------------------------------------------------------------------------------------------
*FROM XML TO SQL (https://dev.mysql.com/doc/refman/8.0/en/load-xml.html)
press "Windows Key" -> search "Services" -> search "MySQL80" -> Right-click -> select "Start"
open "C:\Program Files\MySQL\MySQL Shell 8.0\bin\mysqlsh.exe" (MySQL Shell)
\sql
\connect root@localhost 
USE db;
SHOW TABLES;
DROP TABLE table; (OPTIONAL)
SOURCE "C:/Python/edgar/results/xml/xml.sql";


--------------------------------------------------------------------------------------------
*MAIN SQL STATEMENTS
https://www.w3schools.com/sql/

*ENCODING
SET NAMES 'utf8mb4';
SET CHARACTER SET 'utf8mb4';

*TABLE - CREATE TABLE
CREATE TABLE IF NOT EXISTS file_name1 (
 	column1 VARCHAR(300),
	column2 VARCHAR(300)
)
CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_unicode_ci';

*TABLE - LOAD DATA
LOAD DATA INFILE 'C:/Python/edgar/resources/table/file_name1.txt' INTO TABLE file_name1
CHARACTER SET 'utf8mb4'
FIELDS TERMINATED BY '|' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY '';

*XML - CREATE TABLE
CREATE TABLE IF NOT EXISTS table1 (
	accession VARCHAR(300),
	column1 VARCHAR(300),
	column2 VARCHAR(300)
)
CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_unicode_ci';

*XML - LOAD XML
LOAD XML INFILE 'C:/Python/edgar/resources/xml/file_name1.xml' INTO TABLE table1
CHARACTER SET 'utf8mb4'
ROWS IDENTIFIED BY '<table1>';

*EXPORT TABLE
TABLE table INTO OUTFILE 'C:/Directory/table.txt'
CHARACTER SET 'utf8mb4'
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY '';


--------------------------------------------------------------------------------------------
*TECHNICAL MATERIALS
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
https://www.sec.gov/Archives/edgar/daily-index/
https://www.sec.gov/Archives/edgar/full-index/
https://www.sec.gov/include/ticker.txt
https://www.sec.gov/files/company_tickers.json
https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
https://sraf.nd.edu/

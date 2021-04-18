*INSTALL REQUIREMENTS
pip install -r requirements.txt


--------------------------------------------------------------------------------------------
*STUDY MATERIALS - SEC
https://www.sec.gov/sec-data-resources
https://www.sec.gov/edgar.shtml
https://www.sec.gov/page/corpfin-section-landing
https://www.sec.gov/dera
https://www.sec.gov/search/search.htm (FULL TEXT SEARCH)

*STUDY MATERIALS - LOUGHRAN and MCDONALD
https://sraf.nd.edu/

*STUDY MATERIALS - FILINGS and FORMS
https://www.sec.gov/info/edgar/forms/edgform.pdf
https://www.sec.gov/forms

*STUDY MATERIALS - XBRL
https://www.sec.gov/structureddata/osd-inline-xbrl.html
https://www.sec.gov/dera/data/financial-statement-and-notes-data-set.html
http://xbrlview.fasb.org/yeti/resources/yeti-gwt/Yeti.jsp
https://github.com/TiesdeKok/xbrl-api-playground


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
*DOWNLOAD TXT - FINAL REPORT
fill "resources/txt/"
py main.py -txt

*FROM HTML TO TXT
fill "resources/html/"
py main.py -html

*FROM (DELIMITER-SEPARATED) TABLE TO SQL
fill "resources/table/"
set delimiter (e.g., ","; "|"; "tab")
py main.py -table "tab" 

*FROM XML TO SQL
fill "resources/xml/"
py main.py -xml


--------------------------------------------------------------------------------------------
*SEE RESULTS
see "results/"


--------------------------------------------------------------------------------------------
*GITHUB REPOS
https://github.com/andrewkittredge/financial_fundamentals (from xml to sql)
https://github.com/lukerosiak/pysec (from xml to sql)
https://github.com/tooksoi/ScraXBRL (from xml to sql)

*TECHNICAL MATERIALS
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
https://www.sec.gov/Archives/edgar/daily-index/
https://www.sec.gov/Archives/edgar/full-index/
https://www.sec.gov/include/ticker.txt
https://www.sec.gov/files/company_tickers.json
https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual
https://www.sec.gov/data.json


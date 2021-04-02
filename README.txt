*INSTALL REQUIREMENTS
pip install -r requirements.txt

*STUDY MATERIALS - SEC and FASB
https://www.sec.gov/sec-data-resources
https://www.sec.gov/edgar.shtml
https://www.sec.gov/page/corpfin-section-landing
https://www.sec.gov/dera
https://www.sec.gov/dera/data
https://www.fasb.org/home

*STUDY MATERIALS - FILINGS and FORMS
https://www.sec.gov/info/edgar/forms/edgform.pdf
https://www.sec.gov/forms

*TECHNICAL MATERIALS - FILINGS
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
https://github.com/datasets/edgar
https://github.com/sec-edgar/sec-edgar
https://github.com/alions7000/SEC-EDGAR-text
https://www.sec.gov/Archives/edgar/daily-index/
https://www.sec.gov/Archives/edgar/full-index/
https://www.sec.gov/include/ticker.txt
https://www.sec.gov/files/company_tickers.json
https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual

*TECHNICAL MATERIALS - XBRL
https://www.xbrl.org/the-standard/why/xbrl-for-securities-filing/
https://www.sec.gov/structureddata/osd-inline-xbrl.html
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual
http://xbrlview.fasb.org/yeti/resources/yeti-gwt/Yeti.jsp
https://github.com/Arelle/EdgarRenderer
https://github.com/TiesdeKok/xbrl-api-playground
https://github.com/tooksoi/ScraXBRL







------------------OLD------------------
*PRELIMINARY
fill "resources/varlist.csv"

*CREATE DATABASES
py main.py -a

*CREATE DO FILES AND VARIABLE NAMES
py main.py -b
------------------OLD------------------





TO DO
*DOWNLOAD FILINGS FROM LIST - FINAL REPORT (not-downloaded?)
fill "resources/filings.csv"
py main.py -download
#to "results/filings/txt"
#to "results/filings/txt"
#to "results/filings/html"



*FROM XML FILINGS CREATE SQL DATABASE
fill "resources/xml.csv"
fill "resources/xml_schema.csv"
py main.py -xml
#to "results/sql_statement.txt"


*FROM XBRL FILINGS CREATE SQL DATABASE (https://github.com/search?o=desc&q=xbrl&s=stars&type=Repositories)
fill "resources/xbrl.csv"
fill "resources/xbrl_schema.csv"
py main.py -xbrl
#to "results/filings/xbrl/"

*CONVERT HTML FILINGS INTO TXT (https://github.com/alions7000/SEC-EDGAR-text)
fill "resources/html.csv"
fill "resources/html_schema.csv"
py main.py -html
#to "results/filings/html/"

*SEE RESULTS
see "results/"


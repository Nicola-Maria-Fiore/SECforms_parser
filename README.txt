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
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
https://www.sec.gov/forms

*TECHNICAL MATERIALS - FILINGS
https://github.com/sec-edgar/sec-edgar
https://www.sec.gov/Archives/edgar/daily-index/
https://www.sec.gov/Archives/edgar/full-index/
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm -> 
"XSLT Stylesheets for HTML Rendering of EDGAR XML Filings", "ticker.txt", "company_tickers.json", "Current list of all CIKs matched with entity name"
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
*DOWNLOAD FILINGS FROM LIST
fill "resources/filings.csv", column header "fname"
py main.py -download
#to "results/filings/"

*DOWNLOAD FILINGS FROM LIST - FILINGS REPORT
py main.py -download report
#to "results/filings/filings_report.csv"

*FROM XML FILINGS CREATE SQL DATABASE
fill "resources/filings.csv", column header "xml" dummy
fill "resources/xml_schema.csv"
py main.py -xml
#to "results/xml_query.txt"


*FROM XBRL FILINGS CREATE SQL DATABASE (https://github.com/search?o=desc&q=xbrl&s=stars&type=Repositories)
fill "resources/filings.csv", column header "xbrl" dummy
fill "resources/xbrl_schema.csv"
py main.py -xbrl
#to "results/xbrl_query.txt"

*CONVERT HTML FILINGS INTO TXT (https://stackoverflow.com/questions/14694482/converting-html-to-text-with-python; https://pypi.org/project/html2text/; https://skeptric.com/html-to-text/)
fill "resources/filings.csv", column header "html" dummy
fill "resources/html_schema.csv"
py main.py -html
#to "results/html_query.txt"

*SEE RESULTS
see "results/"


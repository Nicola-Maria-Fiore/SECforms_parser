*INSTALL REQUIREMENTS
pip install -r requirements.txt

*STUDY MATERIALS
https://www.sec.gov/oiea/Article/edgarguide.html
https://www.sec.gov/page/corpfin-section-landing

*TECHNICAL MATERIALS - FORMS
https://www.sec.gov/edgar.shtml -> SEC Forms List (PDF versions) - (https://www.sec.gov/forms)
https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual

*TECHNICAL MATERIALS - XBRL
https://www.xbrl.org/the-standard/why/xbrl-for-securities-filing/
https://www.sec.gov/structureddata/osd-inline-xbrl.html
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual
https://github.com/Arelle/EdgarRenderer




------OLD------
*PRELIMINARY
fill "resources/varlist.csv"

*CREATE DATABASES
py main.py -a

*CREATE DO FILES AND VARIABLE NAMES
py main.py -b
------OLD------






TO DO
*DOWNLOAD FILINGS FROM LIST
fill "resources/filings.csv", column header "fname"
py main.py -download
#to "results/filings/"

*DOWNLOAD FILINGS FROM LIST - FINAL REPORT
py main.py -download report
#to "results/filings/report.csv"

*FROM XML FILINGS CREATE SQL DATABASE
fill "resources/filings.csv", column header "xml" dummy
py main.py -xml
#to "results/xml/"


*FROM XBRL FILINGS CREATE SQL DATABASE (https://github.com/search?o=desc&q=xbrl&s=stars&type=Repositories)
fill "resources/filings.csv", column header "xbrl" dummy
py main.py -xbrl
#to "results/xbrl/"

*CONVERT HTML FILINGS INTO TXT (https://stackoverflow.com/questions/14694482/converting-html-to-text-with-python; https://pypi.org/project/html2text/; https://skeptric.com/html-to-text/)
fill "resources/filings.csv", column header "html" dummy
py main.py -html
#to "results/html/"

*SEE RESULTS
see "results/filings/"
see "results/xml/"
see "results/xbrl/"
see "results/html/"

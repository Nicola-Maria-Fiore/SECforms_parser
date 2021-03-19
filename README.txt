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
compile file "resources/varlist.csv"

*CREATE DATABASES
py main.py -a

*CREATE DO FILES AND VARIABLE NAMES
py main.py -b
------OLD------






TO DO
*DOWNLOAD FILINGS FROM LIST
compile resources/filings.csv (ex varlist)
py main.py -download

*DOWNLOAD FILINGS FROM LIST - FINAL REPORT
py main.py -download report

*FROM XML FILINGS CREATE SQL DATABASE
compile resources/xml_filings.csv
py main.py -xml

*FROM XBRL FILINGS CREATE SQL DATABASE (https://github.com/search?o=desc&q=xbrl&s=stars&type=Repositories)
compile resources/xbrl_filings.csv
py main.py -xbrl

*CONVERT HTML FILINGS INTO TXT (https://stackoverflow.com/questions/14694482/converting-html-to-text-with-python; https://pypi.org/project/html2text/; https://skeptric.com/html-to-text/)
compile resources/html_filings.csv
py main.py -html

*SEE RESULTS
see "results/download"
see "results/xml"
see "results/xbrl"
see "results/html"

*INSTALL REQUIREMENTS
pip install -r requirements.txt

*STUDY MATERIALS
https://www.sec.gov/oiea/Article/edgarguide.html
https://www.investor.gov/introduction-investing/investing-basics/role-sec/laws-govern-securities-industry
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

*GITHUB REPOSITORIES - EDGAR
https://github.com/search?o=desc&q=edgar&s=stars&type=Repositories

*GITHUB REPOSITORIES - XBRL
https://github.com/search?o=desc&q=edgar&s=stars&type=Repositories

*PRELIMINARY
compile file "resources/varlist.csv"

*CREATE DATABASES
py main.py -a

*CREATE DO FILES AND VARIABLE NAMES
py main.py -b

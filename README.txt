--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*INSTALL REQUIREMENTS
pip install -r requirements.txt


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*PRELIMINARY
*ENCODING
set path in "C:/Python/edgar/"
py encoding.py 

--------------------------------------------------------------------------------------------
*FUNCTIONS
*DOWNLOAD TXT
fill "resources/txt/txt.dta", column "fname" (from "WRDS SEC Analytics Suite - SEC Filings on WRDS" https://wrds-web.wharton.upenn.edu/wrds//ds/sec/wforms/filings.cfm)
cd "C:/Python/edgar/resources/txt/"
py txt.py

*FROM HTML TO TXT
fill "resources/html/files/"
cd "edgar/resources/html/"
py html.py

*FROM (DELIMITER-SEPARATED) TABLE TO SQL
fill "resources/table/files/"
set delimiter and encloser in "C:/Python/edgar/resources/table/table.py"
cd "C:/Python/edgar/resources/table/"
py table.py

*FROM XML TO SQL
fill "C:/Python/edgar/resources/xml/files/"
fill "C:/Python/edgar/resources/xml/schema/" (file name as table, list Element Names)
fill "C:/Python/edgar/resources/xml/clean.csv/" (remove "NV" Element Names)
cd "C:/Python/edgar/resources/xml/"
py clean.py
py xml.py


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*SEE RESULTS
see "results/"


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*STUDY MATERIALS
*DATA.GOV
https://www.data.gov/


--------------------------------------------------------------------------------------------
*WRDS SEC ANALYTICS SUITE
https://wrds-www.wharton.upenn.edu/pages/get-data/wrds-sec-analytics-suite/
https://wrds-web.wharton.upenn.edu/wrds//ds/sec/wforms/filings.cfm


--------------------------------------------------------------------------------------------
*SEC
*DATA
https://www.sec.gov/sec-data-resources
https://www.sec.gov/dera/data
https://www.sec.gov/info/edgar/siccodes.htm
https://www.sec.gov/search/search.htm (FULL TEXT SEARCH)

*DIVISIONS & OFFICES
https://www.sec.gov/divisions.shtml
https://www.sec.gov/page/corpfin-section-landing
https://www.sec.gov/page/enforcement-section-landing
https://www.sec.gov/investment-management
https://www.sec.gov/dera
https://www.sec.gov/divisions/trading-markets

*ENFORCEMENT
https://www.sec.gov/page/litigation
https://www.sec.gov/litigations/sec-action-look-up

*REGULATION
https://www.sec.gov/page/regulation
https://www.investor.gov/introduction-investing/investing-basics/role-sec/laws-govern-securities-industry
https://www.investor.gov/introduction-investing/investing-basics/role-sec/researching-federal-securities-laws-through-sec

*EDUCATION
https://www.investor.gov/
https://www.investor.gov/introduction-investing/getting-started/researching-investments
https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work
https://www.investor.gov/introduction-investing/investing-basics/glossary

*FILINGS
https://www.sec.gov/edgar.shtml
https://www.sec.gov/forms
https://www.sec.gov/info/edgar/forms/edgform.pdf
https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications
https://www.sec.gov/edgar/filer-information/current-edgar-filer-manual
https://www.sec.gov/structureddata/osd-inline-xbrl.html
http://xbrlview.fasb.org/yeti/resources/yeti-gwt/Yeti.jsp
https://github.com/TiesdeKok/xbrl-api-playground

*FINRA
https://www.finra.org/#/
https://www.finra.org/investors/tools-and-calculators
http://finra-markets.morningstar.com/MarketData/
https://tools.finra.org/fund_analyzer/


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------
*TECHNICAL MATERIALS
https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm
https://www.sec.gov/Archives/edgar/daily-index/
https://www.sec.gov/Archives/edgar/full-index/
https://www.sec.gov/include/ticker.txt
https://www.sec.gov/files/company_tickers.json
https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
https://sraf.nd.edu/

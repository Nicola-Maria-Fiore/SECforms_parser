import os
import sys
from bs4 import BeautifulSoup
import shutil
import pandas as pd
import csv
import inspect
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin
import requests
import time

#TO_CSV
to_csv=dict(sep=',', na_rep='.', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding="utf-8-sig", compression='infer', quoting=csv.QUOTE_ALL, quotechar='"', line_terminator='\r\n', chunksize=10000, date_format=None, doublequote=True, escapechar='\\', decimal='.', errors='strict', storage_options=None)
#READ_CSV
read_csv=dict(sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=str, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True, escapechar='\\', comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)

#GLOBALS
report=None
path_resources=None
path_results=None
dir=None


############################################################################
#PRELIMINARY
#DIRECTORY
def directory(function_name):
    global path_resources
    global path_results
    global dir
    #FOLDERS
    current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
    path_resources=current_dir+"resources/"+function_name+"/"
    os.chdir(path_resources)
    path_results=path_resources.replace("resources", "results")
    dir=path_results+"files/"
#DOWNLOAD - SWITCH
def re_download(path_results, dir):
    shutil.rmtree(path_results, ignore_errors=True)
    os.mkdir(path_results)
    os.mkdir(dir)


############################################################################
#UTILS
def gen_report():
    report.index.name="index"
    file_path=path_results+"report.csv"
    report.to_csv(path_or_buf=file_path, **to_csv)
    print("report.csv - done")
def requests_retry_session(
    retries=5,
    backoff_factor=0.3,
    status_forcelist=(400,403,408,409,413,429,440,500,502,503,504,509),
    session=None,):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
#ENCODING
def encoding(path):
    charset="utf-8-sig"
    path_resources="C:/Python/edgar/resources/"+path+"/files/"
    path_results="C:/Python/edgar/resources/"+path+"/encoding/"
    dirs=os.listdir(path_resources)
    for i,value in enumerate(dirs):
        file_path=path_resources+value
        with open(file_path, 'r') as f:
            unicode_text=f.read()
            encoded_unicode = unicode_text.encode(charset)
        file_path=path_results+value
        with open(file_path, 'wb') as f:
            f.write(encoded_unicode)
            f.close()  
        print(f"{i} - {value}")
    print("encoding - done")
#CLEAN
def clean():
    path_resources="C:/Python/edgar/resources/xml/"
    path_results="C:/Python/edgar/resources/xml/clean/"
    #DOWNLOAD - SWITCH
    shutil.rmtree(path_results, ignore_errors=True)
    os.mkdir(path_results)
    #ENCODING FOLDER - SET
    encoding_dir=path_resources+"encoding/"
    dirs=os.listdir(encoding_dir)
    #CLEAN
    edgar_old="<edgarSubmission>\n"
    for i,value in enumerate(dirs):
        file_path=encoding_dir+value
        with open(file_path, 'r') as f:
            text=f.read()
        df=pd.read_csv(path_resources+"clean.csv", warn_bad_lines=True, error_bad_lines=False, engine='python')
        columns=df["Element Name"].tolist()
        for c, col in enumerate(columns):
            column=columns[c]
            old_1="<"+column+">"
            old_2="</"+column+">"
            text=text.replace(old_1, "").replace(old_2, "")
        acc=value.split("_",1)[1].split(".",1)[0]
        edgar_new=edgar_old+"<accession>"+acc+"</accession>\n"
        text=text.replace(edgar_old,edgar_new)
        file_path=path_results+value
        with open(file_path, 'w') as f:
            f.write(text)
            f.close()  
        print(f"{i} - {value}")
    print("clean - done")


############################################################################
#EDGAR TOOLS
#HTML
def HTML():
    #GLOBALS
    global report
    #DIRECTORY
    function_name=inspect.stack()[0][3]
    directory(function_name)
    #DOWNLOAD - SWITCH
    re_download(path_results, dir)
    #ENCODING FOLDER
    encoding(function_name)
    encoding_dir=path_resources+"encoding/"
    dirs=os.listdir(encoding_dir)
    #HTMLtoTEXT
    def HTMLtoTEXT(html_doc):
        soup=BeautifulSoup(html_doc, 'html.parser')
        content=soup.text.split(" ")
        content=[c for c in content if len(c)<=30]
        return " ".join(content)
    #HTML
    report=pd.DataFrame(columns=["value","downloaded"])
    for i,value in enumerate(dirs):
        downloaded=False
        if value.endswith(".html") or value.endswith(".htm") or value.endswith(".txt"):
            with open(os.path.join(encoding_dir, value), 'r') as f:
                content=f.read()
            res=HTMLtoTEXT(content)
            with open(os.path.join(dir, value), 'w') as f:
                f.write(res)
            downloaded=True
        report.loc[i]=[value, downloaded]
        print(f"{i} - {value}")
    print("done")   
    gen_report()

#TABLE
def table():
    #DIRECTORY
    function_name=inspect.stack()[0][3]
    directory(function_name)
    #DOWNLOAD - SWITCH
    re_download(path_results, dir)
    #ENCODING FOLDER - SET
    encoding_dir=path_resources+"encoding/"
    dirs=os.listdir(encoding_dir)
    #FACTSET - CHANGE
    delimiter=r"|"
    encloser=r'"'
    #EDGAR - CHANGE
    #delimiter=r"\t"
    #encloser=r''
    statement=r"""
    \sql
    \connect root@localhost
    DROP DATABASE IF EXISTS db;
    CREATE DATABASE IF NOT EXISTS db;
    USE db;
    """
    for i,value in enumerate(dirs):
        tname=os.path.splitext(value)[0]
        abs_path=os.path.abspath(encoding_dir+value).replace("\\","/")
        #READ CSV
        df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
        columns=list(df.columns)
        cols=[]
        for c in range(len(columns)):
            column=columns[c]
            cols.append( "\t" + column + " VARCHAR(300)")
        col_statement=",\n".join(cols)
        #CREATE TABLE
        create_statement=r"""
    CREATE TABLE IF NOT EXISTS {} (
    {}
    )
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_unicode_ci';
        """.format(tname, col_statement)
        #LOAD DATA
        encloser_load=encloser.replace("None","")
        load_statement=r"""
        LOAD DATA INFILE '{}' REPLACE INTO TABLE {}
        CHARACTER SET 'utf8mb4'
        FIELDS TERMINATED BY '{}' ENCLOSED BY '{}' ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n' STARTING BY ''
        IGNORE 1 LINES;
        """.format(abs_path, tname, delimiter, encloser_load)
        statement=statement+create_statement+load_statement
        print(f"{i} - {value}")
    with open(path_results+"table.sql", 'w', encoding='utf-8-sig') as f:
        f.write(statement)
        f.close()
    print("done")

#TXT
def txt():
    #GLOBALS
    global report
    #DIRECTORY
    function_name=inspect.stack()[0][3]
    directory(function_name)
    #DOWNLOAD - SWITCH
    re_download(path_results, dir)
    #TXT
    req=requests_retry_session() 
    HEADERS={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    base_url="https://www.sec.gov/Archives/"
    df=pd.read_stata(path_resources+"txt.dta")
    report=pd.DataFrame(columns=["file_name","not_downloaded"])
    for i in df.index.values:
        file_name=df.loc[i,"fname"]
        value=file_name
        file_path=dir+file_name.replace("edgar/data/","").replace("/","_")
        downloaded=False
        if os.path.isfile(file_path):
            downloaded=True
            print(f"{i} - {value} - already downloaded")
        else:
            url = urljoin(base_url, file_name)
            try:
                r=req.get(url, headers=HEADERS)
                if r.status_code==200:
                    file_path=dir+file_name.replace("edgar/data/","").replace("/","_")
                    with open(file_path, "w") as f:
                        f.write(r.text)
                    print(f"{i} - {value}")
                    downloaded=True
                    time.sleep(1/10)
                elif r.status_code == 404:
                    #https://developer.edgar-online.com/docs/errors
                    print(f"{i} - {value} - not found") 
                    print(r.status_code)  
                    pass               
                else:
                    print(f"{i} - {value} - error")
                    print(r.status_code)
                    pass
            except Exception as e:
                print(f"{i} - {value} - error")
                print(r.status_code)
                print(e)
                pass
        report.loc[i]=[file_name, downloaded]
    print("done")
    gen_report()     

#XML
def xml():
    #GLOBALS
    global report
    #DIRECTORY
    function_name=inspect.stack()[0][3]
    directory(function_name)
    #DOWNLOAD - SWITCH
    re_download(path_results, dir)
    #ENCODING FOLDER
    encoding(function_name)
    encoding_dir=path_resources+"encoding/"
    dirs=os.listdir(encoding_dir)
    #CLEAN
    clean()
    #XML
    current_dir_schema=path_resources+"schema/"
    dir_schema=os.listdir(current_dir_schema)
    current_dir_clean=path_resources+"/clean/"
    dir_clean=os.listdir(current_dir_clean)
    delimiter=","
    encloser='"'
    statement=r"""
    \sql
    \connect root@localhost
    DROP DATABASE IF EXISTS db;
    CREATE DATABASE IF NOT EXISTS db;
    USE db;
    """
    for j,valuej in enumerate(dir_schema):
        tname=os.path.splitext(valuej)[0]
        abs_path=os.path.abspath(current_dir_schema+valuej).replace("\\","/")
        #READ CSV
        df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
        columns=df["Element Name"].tolist()
        cols=[]
        for c,column in enumerate(columns):
            cols.append( "\t" + column + " VARCHAR(300)")
        col_statement=",\n".join(cols)
        #CREATE TABLE
        create_statement=r"""
    CREATE TABLE IF NOT EXISTS {} (
    {}
    )
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_unicode_ci';
        """.format(tname, col_statement)
        statement=statement+create_statement
        for i,value in enumerate(dir_clean):
            #LOAD XML
            abs_path=os.path.abspath(current_dir_clean+value).replace("\\","/")
            load_statement=r"""
        LOAD XML INFILE '{}' REPLACE INTO TABLE {}
        CHARACTER SET 'utf8mb4'
        ROWS IDENTIFIED BY '<{}>';
            """.format(abs_path, tname, tname)
            statement=statement+load_statement
            print(f"{i} - {value}")
        with open(path_results+"xml.sql", 'w', encoding='utf-8-sig') as f:
            f.write(statement)
            f.close()
    print("done")


############################################################################
#EDGAR TOOLS
HTML()
table()
txt()
xml()
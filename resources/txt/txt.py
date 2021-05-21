from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin
import pandas as pd
import os
import requests
from time import sleep
import csv

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
req=requests_retry_session() 

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
base_url = "https://www.sec.gov/Archives/"

current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
os.chdir(current_dir)
path_results=current_dir.replace("resources", "results")
if os.path.isdir(path_results)==False:
    os.mkdir(path_results)
dir=path_results+"txt/"
if os.path.isdir(dir)==False:
    os.mkdir(dir)

df=pd.read_stata(current_dir+"txt.dta")
report=pd.DataFrame(columns=["file_name","not_downloaded"])
for i in df.index.values:
    file_name=df.loc[i,"fname"]
    file_path=dir+file_name.replace("edgar/data/","").replace("/","_")
    if os.path.isfile(file_path):
        downloaded=True
        not_downloaded=0
        print("{} - {} - already downloaded".format(str(i),file_name))
    else:
        downloaded=False
        not_downloaded=1
        url = urljoin(base_url, file_name)
        try:
            r=req.get(url, headers=HEADERS)
            if r.status_code==200:
                file_path=dir+file_name.replace("edgar/data/","").replace("/","_")
                with open(file_path, "w") as f:
                    f.write(r.text)
                print("{} - {}".format(str(i), file_name))
                downloaded=True
                not_downloaded=0
                sleep(1/10)
            elif r.status_code == 404:
                #https://developer.edgar-online.com/docs/errors
                print("{} - {} - not found".format(str(i), file_name)) 
                print(r.status_code)                 
            else:
                print("{} - {} - error".format(str(i), file_name)) 
                print(r.status_code)
        except Exception as e:
            print("{} - {} - error".format(str(i), file_name)) 
            print(r.status_code)
            print(str(e))
            break
    report.loc[i]=[file_name,not_downloaded]
report.to_csv(path_results+"report.csv", sep=',', quotechar='"', quoting=csv.QUOTE_ALL, encoding="utf-8-sig")
print("report.csv - done") 
print("done")         

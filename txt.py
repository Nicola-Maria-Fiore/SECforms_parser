import pandas as pd
from urllib.parse import urljoin
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
import time

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
base_url = "https://www.sec.gov/Archives/"

database = "resources/txt/txt.dta"
txt_report = "results/txt/report.dta"

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


def main():
    df = pd.read_stata(database)
    req = requests_retry_session()
    for i in df.index.values:
        file_name = df.loc[i,"fname"]
        fpath = "results/txt/" + file_name.replace("edgar/data/","").replace("/","_")
        if os.path.isfile(fpath):
            print("{} - {} - already downloaded".format(str(i),file_name))
        else:
            url = urljoin(base_url, file_name)
            try:
                time.sleep(1/20)
                r = req.get(url, headers=HEADERS)
                if r.status_code == 200:
                    new_file = "results/txt/" + file_name.replace("edgar/data/","").replace("/","_")
                    with open(new_file, "w") as f:
                        f.write(r.text)
                    print("{} - {} - done".format(str(i), file_name))
                else:
                    #https://developer.edgar-online.com/docs/errors
                    if r.status_code == 404:
                        print("{} - {} - not found".format(str(i), file_name))
                    else:
                        raise Exception() 
            except Exception as e:
                print(str(e))
                print(str(r.status_code))
                print("restart router")
                break


def checkFiles():
    df = pd.read_stata(database)
    for i in df.index.values:
        file_name = df.loc[i,"fname"]
        fpath = "results/txt/" + file_name.replace("edgar/data/","").replace("/","_")
        print("{} - {} checking".format(str(i), file_name))
        if os.path.isfile(fpath):
            df.loc[i,"not_downloaded"] = 0
        else:
            df.loc[i,"not_downloaded"] = 1
    df.to_stata(txt_report)
            

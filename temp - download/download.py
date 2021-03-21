import pandas as pd
import psutil
import sys
from urllib.parse import urljoin
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
import os
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
base_url = "https://www.sec.gov/Archives/"
database = "resources/database.dta"
database_check = "resources/database_check.dta"

def requests_retry_session(
    retries=5,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 503, 504, 509),
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
    start = int(input("Starting from: "))
    req = requests_retry_session()

    for i in df.index.values:
        if i < start:
            continue

        file_name = df.loc[i,"FName"]

        url = urljoin(base_url, file_name)

        try:
            r = req.get(url, headers=HEADERS)
            if r.status_code == 200:
                new_file = "results/" + file_name.replace("edgar/data/","").replace("/","_")
                with open(new_file, "w") as f:
                    f.write(r.text)
                print("Downloaded record {}".format(str(i)))
            else:
                if r.status_code == 404:
                    print("Record {} not found".format(str(i)))
                else:
                    raise Exception() 

        except Exception as e:
            print(e)
            print("Restart router")
            break


def checkFiles():
    df = pd.read_stata(database)
    for i in df.index.values:
        print("Checking "+str(i))
        file_name = df.loc[i,"FName"]
        fpath = "results/" + file_name.replace("edgar/data/","").replace("/","_")
        if os.path.isfile(fpath):
            df.loc[i,"downloaded"] = 1
        else:
            df.loc[i,"downloaded"] = 0
    df.to_stata(database_check)
            

if __name__ =="__main__":
    if len(sys.argv)< 2:
        print("Invalid operation")
        sys.exit()

    if (sys.argv[1]=="-a"):
        hdd = psutil.disk_usage('/')
        if (hdd.free / (2**30)) < 20:
            print("Not enough space")
            sys.exit()
        main()
    elif (sys.argv[1]=="-b"):
        checkFiles()

    print("Done!")
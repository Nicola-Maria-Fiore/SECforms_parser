from bs4 import BeautifulSoup
import os
import pandas as pd
import csv

def HTMLtoTEXT(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    content = soup.text.split(" ")
    content = [c for c in content if len(c)<=30]
    return " ".join(content)

current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
os.chdir(current_dir)
path_results=current_dir.replace("resources", "results")
if os.path.isdir(path_results)==False:
    os.mkdir(path_results)
dir=path_results+"html/"
if os.path.isdir(dir)==False:
    os.mkdir(dir)

current_dir=current_dir+"encoding"

report=pd.DataFrame(columns=["value","not_downloaded"])
dirs=os.listdir(current_dir)
for i,value in enumerate(dirs):
    downloaded=False
    not_downloaded=1
    if value.endswith(".html") or value.endswith(".htm") or value.endswith(".txt"):
        with open(os.path.join(current_dir, value), 'r') as f:
            content=f.read()
        res=HTMLtoTEXT(content)
        with open(os.path.join(dir, value), 'w') as f:
            f.write(res)
        downloaded=True
        not_downloaded=0
    report.loc[i]=[value,not_downloaded]
    print("{} - {}".format(str(i), value))
report.to_csv(path_results+"report.csv", sep=',', quotechar='"', quoting=csv.QUOTE_ALL, encoding="utf-8-sig")
print("report.csv - done")  
print("done")
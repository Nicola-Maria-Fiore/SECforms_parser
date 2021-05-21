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

report=pd.DataFrame(columns=["file_name","not_downloaded"])
counter=0
dirs=os.listdir(current_dir)
for d in range(len(dirs)):
    file_name=dirs[d]
    downloaded=False
    not_downloaded=1
    if file_name.endswith(".html") or file_name.endswith(".htm") or file_name.endswith(".txt"):
        with open(os.path.join(current_dir, file_name), 'r') as f:
            content=f.read()
        res=HTMLtoTEXT(content)
        with open(os.path.join(dir, file_name), 'w') as f:
            f.write(res)
        downloaded=True
        not_downloaded=0
    report.loc[counter]=[file_name,not_downloaded]
    counter+=1
report.to_csv(path_results+"report.csv", sep=',', quotechar='"', quoting=csv.QUOTE_ALL, encoding="utf-8-sig")
print("report.csv - done")  
print("done")
import os
import pandas as pd

current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
os.chdir(current_dir)
path_results=current_dir.replace("resources", "results")
if os.path.isdir(path_results)==False:
    os.mkdir(path_results)

current_dir_encoding=current_dir+"encoding/"
dir_encoding=os.listdir(current_dir_encoding) 
edgar_old="<edgarSubmission>\n"
for i,value in enumerate(dir_encoding):
    file_path=current_dir_encoding+value
    with open(file_path, 'r') as f:
        text=f.read()
    df=pd.read_csv(current_dir+"clean.csv", warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=df["Element Name"].tolist()
    for c in range(len(columns)):
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
    print("{} - {}".format(str(i), value))
print("done")

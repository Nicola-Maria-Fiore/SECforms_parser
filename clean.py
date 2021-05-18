import os
import pandas as pd

path_resources="resources/xml/encoding/"
path_results="resources/xml/clean/"

dirs=os.listdir(path_resources)
dirs.remove('.keep')   
i=0
edgar_old="<edgarSubmission>\n"
for file in dirs:
    input_file=path_resources+file
    with open(input_file, 'r') as f:
        text=f.read()
    
    df=pd.read_csv("resources/xml/clean.csv", warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=df["Element Name"].tolist()
    for column in columns:
        old_1="<"+column+">"
        old_2="</"+column+">"
        text=text.replace(old_1, "").replace(old_2, "")

    acc=file.split("_",1)[1].split(".",1)[0]
    edgar_new=edgar_old+"<accession>"+acc+"</accession>\n"
    text=text.replace(edgar_old,edgar_new)

    out_file=path_results+file
    with open(out_file, 'w') as f:
        f.write(text)
        f.close()  
    print("{} - {}".format(str(i), input_file))
    i=i+1

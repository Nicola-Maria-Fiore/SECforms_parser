import os
import pandas as pd

path_resources="resources/xml/encoding/"
path_results="resources/xml/clean/"

dirs=os.listdir(path_resources)
    
i=0
for file in dirs:  
    input_file=path_resources+file
    with open(input_file, 'r') as f:
        text=f.read()
    
    df=pd.read_csv("resources/xml/schema/clean.csv", warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=df["Element Name"].tolist()
    for column in columns:
        old_1="<"+column+">"
        old_2="</"+column+">"
        text=text.replace(old_1, "").replace(old_2, "")

    out_file=path_results+file
    with open(out_file, 'w') as f:
        f.write(text)
        f.close()  
    print("{} - {}".format(str(i), input_file))
    i=i+1

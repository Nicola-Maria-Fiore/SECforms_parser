import pandas as pd
import os

create_statement = ""
insert_statement = ""

def CSVtoSQL(file, delimiter):
    df = pd.read_csv(file, delimiter)

def main(separator):
    source_folder = "resources/xml"
    out_folder = "results/xml"

    for filename in os.listdir(source_folder):
        if filename.endswith(".xml"):
            res = XMLtoSQL(os.path.join(source_folder, filename), separator)
            with open(os.path.join(out_folder, filename), 'w') as f:
                f.write(res)       
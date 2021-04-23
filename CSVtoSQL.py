import pandas as pd
import os
import re


def genCREATE(columns, row, tname):
    create_statement = "CREATE TABLE IF NOT EXISTS {} (\n {} \n);\n\n"
    sql_fields = []
    for col in columns:
        sql_fields.append( "\t" + col + " varchar(300)")

    return create_statement.format(tname,",\n".join(sql_fields))

def genINSERT(records, cols, tname):
    all_records = ""
    insert_statement = "INSERT INTO {} ({}) VALUES ({});\n\n"
    cols = ",".join(cols)
    for r in records:
        all_records += insert_statement.format(tname,cols,r)
    
    return all_records

def CSVtoSQL(f, delimiter, tname):
    tname = re.sub(r'_.*','',tname)
    create_statement = None
    insert_statement = None

    records = []
    df = pd.read_csv(f, sep=delimiter, warn_bad_lines=True, error_bad_lines=False)
    for index, row in df.iterrows():
        if create_statement == None:
            create_statement = genCREATE(list(df.columns), row, tname)          
        record = []
        for col in df.columns:
            record.append('"'+str(row[col]).replace('"','').replace("'",'')+'"')
        records.append(",".join(record))
    
    insert_statement = genINSERT(records, list(df.columns), tname)
    return create_statement + insert_statement


def main(separator):
    full_sql = ""
    source_folder = "resources/table"
    out_folder = "results/table"

    for filename in os.listdir(source_folder):
        if not filename.endswith(".keep"):
            print("-{}".format(filename))
            res = CSVtoSQL(os.path.join(source_folder, filename), separator, filename)
            full_sql += res
            filename = re.sub(r'\..*','.sql',filename)
            with open(os.path.join(out_folder, filename), 'w', encoding='utf-8') as f:
                f.write(res) 

    with open(os.path.join(out_folder, "data.sql"), 'w', encoding='utf-8') as f:
        f.write(full_sql)       

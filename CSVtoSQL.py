import pandas as pd
import os
import re

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


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
    df = pd.read_csv(f, sep=delimiter, warn_bad_lines=True, error_bad_lines=False, engine='python')
    total_it = len(df.index)
    current_it = 0
    for index, row in df.iterrows():
        current_it += 1
        if current_it%100==0:
            printProgressBar(current_it,total_it)
        
        if create_statement == None:
            create_statement = genCREATE(list(df.columns), row, tname)          
        record = []
        for col in df.columns:
            record.append('"'+str(row[col]).replace('"','').replace("'",'')+'"')
        records.append(",".join(record))
    printProgressBar(total_it,total_it)
    
    insert_statement = genINSERT(records, list(df.columns), tname)
    return create_statement + insert_statement


def main(separator):
    source_folder = "resources/table"
    out_folder = "results/table"

    for filename in os.listdir(source_folder):
        if not filename.endswith(".keep"):
            print("-{}".format(filename))
            res = CSVtoSQL(os.path.join(source_folder, filename), separator, filename)
            filename = re.sub(r'\..*','.sql',filename)
            with open(os.path.join(out_folder, filename), 'w', encoding='utf-8') as f:
                f.write(res) 

            with open(os.path.join(out_folder, "table.sql"), 'a', encoding='utf-8') as f:
                f.write(res)       

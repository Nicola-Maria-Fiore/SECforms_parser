import os
import pandas as pd

current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
os.chdir(current_dir)
path_results=current_dir.replace("resources", "results")
if os.path.isdir(path_results)==False:
    os.mkdir(path_results)  

current_dir_encoding=current_dir+"encoding/"
dir_encoding=os.listdir(current_dir_encoding)

#FACTSET
delimiter=r"|"
encloser=r'"'

#EDGAR
#delimiter=r"\t"
#encloser=r''

statement=r"""
\sql
\connect root@localhost
DROP DATABASE IF EXISTS db;
CREATE DATABASE IF NOT EXISTS db;
USE db;
"""

for i,value in enumerate(dir_encoding):
    tname=os.path.splitext(value)[0]
    abs_path=os.path.abspath(current_dir_encoding+value).replace("\\","/")
    #READ CSV
    df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=list(df.columns)
    cols=[]
    for c in range(len(columns)):
        column=columns[c]
        cols.append( "\t" + column + " VARCHAR(300)")
    col_statement=",\n".join(cols)
    #CREATE TABLE
    create_statement=r"""
CREATE TABLE IF NOT EXISTS {} (
{}
)
CHARACTER SET 'utf8mb4'
COLLATE 'utf8mb4_unicode_ci';
    """.format(tname, col_statement)
    #LOAD DATA
    encloser_load=encloser.replace("None","")
    load_statement=r"""
    LOAD DATA INFILE '{}' REPLACE INTO TABLE {}
    CHARACTER SET 'utf8mb4'
    FIELDS TERMINATED BY '{}' ENCLOSED BY '{}' ESCAPED BY '\\'
    LINES TERMINATED BY '\r\n' STARTING BY ''
    IGNORE 1 LINES;
    """.format(abs_path, tname, delimiter, encloser_load)
    statement=statement+create_statement+load_statement
    print("{} - {}".format(str(i), value))
with open(path_results+"table.sql", 'w', encoding='utf-8-sig') as f:
    f.write(statement)
    f.close()
print("done")


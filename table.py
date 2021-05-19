import os
import pandas as pd

path_resources="resources/table/encoding/"
rel_path=os.listdir(path_resources)
rel_path.remove('.keep')

delimiter="|"
encloser='"'

statement=r"""
\sql
\connect root@localhost
DROP DATABASE IF EXISTS db;
CREATE DATABASE IF NOT EXISTS db;
USE db;
"""

i=0
for file in rel_path:
    tname=os.path.splitext(file)[0]
    abs_path=os.path.abspath(path_resources+file).replace("\\","/")

    #READ CSV
    df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=list(df.columns)
    cols=[]
    for column in columns:
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
    load_statement=r"""
    LOAD DATA INFILE '{}' REPLACE INTO TABLE {}
    CHARACTER SET 'utf8mb4'
    FIELDS TERMINATED BY '{}' ENCLOSED BY '{}' ESCAPED BY '\\'
    LINES TERMINATED BY '\r\n' STARTING BY ''
    IGNORE 1 LINES;
    """.format(abs_path, tname, delimiter, encloser)
    statement=statement+create_statement+load_statement
    print("{} - {}".format(str(i), file))
    i=i+1

path_results="results/table/"
with open(path_results+"table.sql", 'w', encoding='utf-8-sig') as f:
    f.write(statement)
    f.close()


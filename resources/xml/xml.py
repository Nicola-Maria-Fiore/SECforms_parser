import os
import pandas as pd

#DIRECTORY
current_dir=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
os.chdir(current_dir)
path_results=current_dir.replace("resources", "results")
shutil.rmtree(path_results)
os.mkdir(path_results)

current_dir_schema=current_dir+"schema/"
dir_schema=os.listdir(current_dir_schema)
current_dir_clean=current_dir+"/clean/"
dir_clean=os.listdir(current_dir_clean)

delimiter=","
encloser='"'
statement=r"""
\sql
\connect root@localhost
DROP DATABASE IF EXISTS db;
CREATE DATABASE IF NOT EXISTS db;
USE db;
"""

for j,valuej in enumerate(dir_schema):
    tname=os.path.splitext(valuej)[0]
    abs_path=os.path.abspath(current_dir_schema+valuej).replace("\\","/")
    #READ CSV
    df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
    columns=df["Element Name"].tolist()
    cols=[]
    for c,column in enumerate(columns):
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
    statement=statement+create_statement
    for i,value in enumerate(dir_clean):
        #LOAD XML
        abs_path=os.path.abspath(current_dir_clean+value).replace("\\","/")
        load_statement=r"""
    LOAD XML INFILE '{}' REPLACE INTO TABLE {}
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<{}>';
        """.format(abs_path, tname, tname)
        statement=statement+load_statement
        print("{} - {}".format(str(i), value))
    with open(path_results+"xml.sql", 'w', encoding='utf-8-sig') as f:
        f.write(statement)
        f.close()
print("done")

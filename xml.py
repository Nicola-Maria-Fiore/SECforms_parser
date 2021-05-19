import os
import pandas as pd

def main():
    path_resources_schema="resources/xml/schema/"
    rel_path_schema=os.listdir(path_resources_schema)
    rel_path_schema.remove('.keep')

    path_resources_clean="resources/xml/clean/"
    rel_path_clean=os.listdir(path_resources_clean)
    rel_path_clean.remove('.keep')

    delimiter=","
    encloser='"'

    statement=r"""
\sql
\connect root@localhost
DROP DATABASE IF EXISTS db;
CREATE DATABASE IF NOT EXISTS db;
USE db;
    """

    for f in rel_path_schema:
        tname=os.path.splitext(f)[0]
        abs_path=os.path.abspath(path_resources_schema+f).replace("\\","/")

        #READ CSV
        df=pd.read_csv(abs_path, sep=delimiter, quotechar=encloser, warn_bad_lines=True, error_bad_lines=False, engine='python')
        columns=df["Element Name"].tolist()
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

        statement=statement+create_statement

        i=0
        for file in rel_path_clean:

            #LOAD XML
            abs_path=os.path.abspath(path_resources_clean+file).replace("\\","/")
            load_statement=r"""
    LOAD XML INFILE '{}' REPLACE INTO TABLE {}
    CHARACTER SET 'utf8mb4'
    ROWS IDENTIFIED BY '<{}>';
            """.format(abs_path, tname, tname)
            statement=statement+load_statement
            print("{} - {}".format(str(i), file))
            i=i+1
            
        path_results="results/xml/"
        with open(path_results+"xml.sql", 'w', encoding='utf-8-sig') as f:
            f.write(statement)
            f.close()

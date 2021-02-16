import pandas as pd

label_do = "results/do_files/label.do"
import_do = "results/do_files/import.do"
var_names_file = "results/var_names.csv"


def genLabelDo(dataframes):
    doContent = ""
    count = 1
    df_do = dataframes["main"]
    for col in df_do.columns:
        if col!="id":
            doContent += 'label variable v{} "{}" \n'.format(count,col)
            count += 1
    with open(label_do,'w') as f:
        f.write(doContent)


def genImportDo(dataframes):
    doContent = ''
    for key, _ in dataframes.items():
        doContent += 'import delimited "{}.csv", varnames(1) stringcols(_all) bindquotes(strict) \n save "{}.dta" \n clear all \n'.format(key,key)
    with open(import_do,'w') as f:
        f.write(doContent)


def genVarNamesFile(dataframes):
    new_var = pd.DataFrame(columns=["old_var","new_var"])
    count = 1
    for col in dataframes["main"].columns:
        if col=="id":
            continue
        row = len(new_var.index)
        new_var.loc[row,"old_var"] = col
        new_var.loc[row,"new_var"] = "v"+str(count)
        count += 1

    new_var.index.name='N'
    new_var.to_csv(var_names_file)






def createDoFiles(dataframes):
    genLabelDo(dataframes)
    genImportDo(dataframes)
    genVarNamesFile(dataframes)

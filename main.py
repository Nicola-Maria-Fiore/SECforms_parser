import pandas as pd
import xmltodict
import os
import sys
import csv

files = "resources/xml_files/"
varlist = "resources/varlist.csv"
label_do = "results/do_files/label.do"
import_do = "results/do_files/import.do"
var_names_file = "results/var_names.csv"


global_var_list = []
avoid_list = []
to_add_list = []

dataframes = {}
dataframes_dict = {}
federal_info = None


def cleanXML(xml):
    start = xml.find("<edgarSubmission>")
    end = xml.rfind("</XML>")
    return xml[start:end]


def createDatasets(dataf):
    df = pd.DataFrame(columns=["ID"])
    lastLev = {0:""}

    end = len(dataf.index)
    i = 0
    add_columns = False
    while i < end:
        element = dataf.iloc[i]
        if i+1<end:
            next_el = dataf.iloc[i+1]

        if i<end-1 and next_el["level"]>element["level"]:
            if i == 0:
                lastLev[element["level"]] = element["element_name"]
            else:
                lastLev[element["level"]] = lastLev[element["level"]-1] + "_" + element["element_name"]

            if element["add_columns"] == 1 and element["data_type"]=="NV" and add_columns == False:
                add_columns = True
                to_add_list.append(element["element_name"])

            if (element["level"]-1 == 0):
                df[element["element_name"]] = ""
            else:
                df[lastLev[element["level"]-1]+"_"+element["element_name"]] = ""

        elif i<end-1 and next_el["level"]<element["level"]: 
            if add_columns:
                num = element["occur"] 
                if num>1:
                    k = 1
                    while k<=num:
                        df[lastLev[element["level"]-1]+"_"+element["element_name"]+"_"+str(k)] = ""
                        k += 1
                    add_columns = False
            else:
                df[lastLev[element["level"]-1]+"_"+element["element_name"]] = "" 
            lastLev[element["level"]] = ""

        elif i==end-1 or next_el["level"]==element["level"]:       
            df[lastLev[element["level"]-1]+"_"+element["element_name"]] = ""             
        i += 1
    return df



def parseListSameFile(value, df, idx, baseName): #Limit: array have only simple object as child  ie <a><b></b><b></b></a>
    if value==None or value=="None": #no child
        return

    separator = "_"
    num = 1

    for key, info in value.items():
        if info=="None":
            continue
        if  isinstance(info, str): #only one child
            prop_name = baseName + separator + key + separator + str(num)
            #df.loc[idx,prop_name] = info
            df[idx].update({prop_name:info})
        else:
            for v in info:
                if v==None:
                    continue
                else:
                    prop_name = baseName + separator + key + separator + str(num)
                    #df.loc[idx,prop_name] = str(v)
                    df[idx].update({prop_name:str(v)})
                    num += 1

    
def parseListSeparateFile(value, df, file_id, baseName):    
    if value==None or value=="None": #no child
        return

    num = len(df)
    separator = "_"
    for key, v in value.items():
        prop_name = str(baseName) + str(separator) + str(key)
        if  isinstance(v, str): #only one child
            pass
        elif isinstance(v, list):
            for el in v: #more than one child
                parseDict(el, file_id, df,num, prop_name)
                num += 1
        else:
            parseDict(v, file_id, df,num, prop_name)

def parseDict(xml_dict, fname, df,idx, baseName=""):
    if len(baseName)>0:
        separator = "_"
    else:
        separator = ""

    #df.loc[idx,"ID"] = fname
    if idx>=len(df):
        df.append({"ID":fname})

    for key, value in xml_dict.items():
        prop_name = str(baseName) + str(separator) + str(key)

        if value==None or value=="None" or key in avoid_list :
            continue
        else:
            if key in dataframes:
                parseListSeparateFile(value, dataframes_dict[key], fname, prop_name)
            elif key in to_add_list:
                parseListSameFile(value, df, idx, prop_name)
            elif isinstance(value, str) or (not isinstance(value, dict) and value.isnumeric()):
                #df.loc[idx,prop_name] = value
                df[idx].update({prop_name:value})
            else:
                parseDict(value,fname,df,idx,prop_name)
    try:
            pass
    except Exception as e:
        print("E1 -> "+str(e))  


def getCSVName(_dir, fname):
    count = 2
    new_fname = _dir + fname + ".csv"
    while os.path.isfile(new_fname):
        new_fname = _dir + fname + "_" + str(count) + ".csv"
        count += 1
    return new_fname


def createDoFiles():
    doContent = ""
    count = 1
    df_do = dataframes["main"]
    for col in df_do.columns:
        if col!="ID":
            doContent += '\n label variable {} "v{}"'.format(col,count)
            count += 1
    with open(label_do,'w') as f:
        f.write(doContent)

    doContent = ''
    for key, _ in dataframes.items():
        doContent += 'import delimited "{}.csv", varnames(1) stringcols(_all) bindquotes(strict) \n save "{}.dta" \n clear all \n'.format(key,key)
    with open(import_do,'w') as f:
        f.write(doContent)

    new_var = pd.DataFrame(columns=["old_var","new_var"])
    count = 1
    for col in dataframes["main"].columns:
        if col=="ID":
            continue
        row = len(new_var.index)
        new_var.loc[row,"old_var"] = col
        new_var.loc[row,"new_var"] = "v"+str(count)
        count += 1

    new_var.index.name='N'
    new_var.to_csv(var_names_file)


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Error: incorrect arguments, read the instructions")
        sys.exit()

    df = pd.read_csv(varlist)
    df["level"] = df["level"].apply(pd.to_numeric)

    main_df = createDatasets(df)

    dataframes["main"] = main_df
    dataframes_dict["main"] = []
    for index, row in df.iterrows():
        if row["separate_file"] == 1:
            dataframes[row["element_name"]] = main_df.copy(True)
            dataframes_dict[row["element_name"]] = []
        if row["avoid"] == 1:
            avoid_list.append(row["element_name"])

    if sys.argv[1]=="-a": 
        idx = 0
        for file_name in os.listdir(files):
            print("{} - {}".format(str(idx),file_name))
            file_dir = files + file_name

            with open(file_dir, 'r') as file:
                xml = file.read()

            xml = cleanXML(xml)
            xmldict = xmltodict.parse(xml)
            #parseDict(xmldict, file_name[:-4], dataframes["main"],idx)
            parseDict(xmldict, file_name[:-4], dataframes_dict["main"],idx)
            idx += 1

        for key in dataframes:
            dataframes[key] = pd.DataFrame(dataframes_dict[key], columns=dataframes[key].columns)

        
        for key, value in dataframes.items():
            count = 1
            for col in value.columns:
                if col=="ID":
                    continue
                value = value.rename({col: "v"+str(count)}, axis=1)
                count += 1
            value.index.name='N'
            for col in value.columns:
                value[col] = value[col].astype(str)
            value.to_csv(getCSVName("results/",key),index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    if sys.argv[1]=="-b":
        createDoFiles()

    print("Done!")

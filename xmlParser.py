import pandas as pd
import xmltodict
import os
import sys
import csv

files = "resources/xml_files/"

def cleanXML(xml):
    start = xml.find("<edgarSubmission>")
    end = xml.rfind("</XML>")
    return xml[start:end]

def getCSVName(_dir, fname):
    count = 2
    new_fname = _dir + fname + ".csv"
    while os.path.isfile(new_fname):
        new_fname = _dir + fname + "_" + str(count) + ".csv"
        count += 1
    return new_fname


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
            df[idx].update({prop_name:info})
        else:
            for v in info:
                if v!=None:
                    prop_name = baseName + separator + key + separator + str(num)
                    df[idx].update({prop_name:str(v)})
                    num += 1

    
def parseListSeparateFile(value, df, file_id, baseName,to_add_list, avoid_list, dataframes, dataframes_dict):    
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
                parseDict(el, file_id, df,num,to_add_list, avoid_list, dataframes, dataframes_dict ,prop_name)
                num += 1
        else:
            parseDict(v, file_id, df,num, to_add_list, avoid_list, dataframes, dataframes_dict ,prop_name)


def parseDict(xml_dict, fname, df,idx ,to_add_list, avoid_list, dataframes, dataframes_dict, baseName=""):
    if len(baseName)>0:
        separator = "_"
    else:
        separator = ""

    if idx>=len(df):
        df.append({"ID":fname})

    try:
        for key, value in xml_dict.items():
            prop_name = str(baseName) + str(separator) + str(key)

            if value==None or value=="None" or key in avoid_list :
                continue
            else:
                if key in dataframes:
                    parseListSeparateFile(value, dataframes_dict[key], fname, prop_name,to_add_list, avoid_list,dataframes, dataframes_dict)
                elif key in to_add_list:
                    parseListSameFile(value, df, idx, prop_name)
                elif isinstance(value, str) or (not isinstance(value, dict) and value.isnumeric()):
                    df[idx].update({prop_name:value})
                else:
                    parseDict(value,fname,df,idx,to_add_list, avoid_list, dataframes, dataframes_dict, prop_name)
    except:
        pass 


def Parse(to_add_list, avoid_list, dataframes, dataframes_dict):
    idx = 0
    for file_name in os.listdir(files):
        print("{} - {}".format(str(idx),file_name))
        file_dir = files + file_name

        with open(file_dir, 'r') as file:
            xml = file.read()

        xml = cleanXML(xml)
        xmldict = xmltodict.parse(xml)
        parseDict(xmldict, file_name[:-4], dataframes_dict["main"],idx,to_add_list, avoid_list, dataframes, dataframes_dict)
        idx += 1

    for key in dataframes:
        dataframes[key] = pd.DataFrame(dataframes_dict[key], columns=dataframes[key].columns)
    
    for key, value in dataframes.items():
        print('Saveing {}...'.format(key))
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
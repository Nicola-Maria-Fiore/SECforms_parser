import pandas as pd
import os
import re
import os.path
import xmltodict

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

def cleanXML(xml):
    start = xml.find("<edgarSubmission>")
    end = xml.rfind("</XML>")
    return xml[start:end]


def toFname(fname):
    return re.sub('[^\w\-_\. ]', '_', fname)


def saveListField(key, fname, arr):
    df = pd.DataFrame() 

    if  "relatedPersonInfo" in key:
        df["Executive Officer"] = ""
        df["Director"] = ""
        df["Promoter"] = ""
    
    try:
        idx = 0
        for el in arr:
            if isinstance(el, str):
                df.loc[idx,key] = el
            else:
                for k, value in el.items():
                    if isinstance(value, list):
                        continue
                    elif isinstance(value, str) or value==None:
                        df.loc[idx,k] = value
                    else:
                        newK = key + "_" + k
                        properties = parseDict(value, fname, newK)
                        for name, val in properties:
                            df.loc[idx,name] = val
            idx = idx + 1

        new_dir = "results/"+toFname(fname[:-4])
        if os.path.isdir(new_dir)==False:
            os.mkdir(new_dir)

        df.to_csv(new_dir+"/"+key+".csv")
    except Exception as e:
        print("E2 -> "+str(e))
        pass
    
    return



def parseDict(xml_dict, fname, df, baseName=""):
    separator = ""
    if len(baseName)>0:
        separator = "_"

    res = []
    try:
        for key, value in xml_dict.items():
            prop_name = baseName + separator + key

            if isinstance(value, str) or value==None:
                res.append((prop_name, value))
            elif isinstance(value, list):
                if key in ["state","description"]:
                    continue
                else:
                    saveListField(prop_name, fname, value)
            else:
                res = res + parseDict(value, fname, prop_name)
    except Exception as e:
        print("E1 -> "+str(e))
    return res
        

if __name__ == "__main__":
    
    dir_ = "resources/"
    for filename in os.listdir(dir_):
        #printProgressBar(i,total)
        file_dir = dir_ + file_name

        with open(file_dir, 'r') as file:
            xml = file.read()

        xml = cleanXML(xml)
        xmldict = xmltodict.parse(xml)
        properties = parseDict(xmldict, file_name)
        for name, val in properties:
            df.loc[i,name] = val

    df.to_csv('results/new_dataset.csv')
    
    print("Done")
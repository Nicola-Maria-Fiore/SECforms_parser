import pandas as pd
import os.path
import xmltodict
import os
import re

dataset = "resources/dataset.dta"

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

if __name__ == "__main__":
    result = pd.DataFrame("")
    df = pd.read_stata(dataset)

   for i in df.index.values:
        printProgressBar(i,total)

        file_name = (df.loc[i,"FName"]).replace("edgar/data/","").replace("/","_")
        file_dir = dir_ + file_name

        if os.path.isfile(file_dir)==False:
            continue

        df.loc[i,"Downloaded"] = True
        with open(file_dir, 'r') as file:
            xml = file.read()

        xml = cleanXML(xml)
        xmldict = xmltodict.parse(xml)
        properties = parseDict(xmldict, file_name)
        for name, val in properties:
            df.loc[i,name] = val

    df.to_csv('results/new_dataset.csv')
    
    print("Done")
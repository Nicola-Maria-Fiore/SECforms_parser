from genDataframes import getFieldsList,createDatasets
from genFiles import createDoFiles
from xmlParser import Parse
import pandas as pd
import sys

varlist = "resources/varlist.csv"

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Error: incorrect arguments, read the instructions")
        sys.exit()

    df = pd.read_csv(varlist)
    df["level"] = df["level"].apply(pd.to_numeric)

    all_vars_list, to_add_list = getFieldsList(df)
    avoid_list, dataframes, dataframes_dict = createDatasets(all_vars_list, df)
    

    if sys.argv[1]=="-a": 
        Parse(to_add_list, avoid_list, dataframes, dataframes_dict)

    if sys.argv[1]=="-b":
        createDoFiles(dataframes)

    print("Done!")

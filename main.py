from genDataframes import getFieldsList,createDatasets
from genFiles import createDoFiles
from xmlParser import Parse
import Html
import pandas as pd
import CSVtoSQL
import txt
import sys

varlist = "resources/varlist.csv"

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Error: incorrect arguments, read the instructions")
        sys.exit()
    
    if sys.argv[1]=="-a" or sys.argv[1]=="-b" : 
        df = pd.read_csv(varlist)
        df["level"] = df["level"].apply(pd.to_numeric)

        all_vars_list, to_add_list = getFieldsList(df)
        avoid_list, dataframes, dataframes_dict = createDatasets(all_vars_list, df)

        if sys.argv[1]=="-a":
            Parse(to_add_list, avoid_list, dataframes, dataframes_dict)
        else:
            createDoFiles(dataframes)
    elif sys.argv[1]=="-txt":
        txt.main()
        txt.checkFiles()
    elif sys.argv[1]=="-html":
        Html.main()
    elif sys.argv[1]=="-table" and len(sys.argv)>2:
        delimiter = sys.argv[2] 
        if delimiter == "tab":
            delimiter = '\t'
        CSVtoSQL.main(delimiter)
    else:
        print("Incorrect arguments!")

    print("Done!")

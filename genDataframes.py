import pandas as pd


def getFieldsList(dataf):
    all_vars_list = []
    to_add_list = []
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
                all_vars_list.append(element["element_name"])
            else:
                all_vars_list.append(lastLev[element["level"]-1]+"_"+element["element_name"])

        elif i<end-1 and next_el["level"]<element["level"]: 
            if add_columns:
                num = element["occur"] 
                if num>1:
                    k = 1
                    while k<=num:
                        all_vars_list.append(lastLev[element["level"]-1]+"_"+element["element_name"]+"_"+str(k))
                        k += 1
                    add_columns = False
            else:
                all_vars_list.append(lastLev[element["level"]-1]+"_"+element["element_name"])
            lastLev[element["level"]] = ""

        elif i==end-1 or next_el["level"]==element["level"]:       
            all_vars_list.append(lastLev[element["level"]-1]+"_"+element["element_name"])             
        i += 1
    return all_vars_list, to_add_list



def createDatasets(all_vars_list, df):
    dataframes = {}
    dataframes_dict = {}
    avoid_list = []

    all_vars_list = ["id"] + all_vars_list
    main_df = pd.DataFrame(columns=all_vars_list)

    dataframes["main"] = main_df
    dataframes_dict["main"] = []
    for index, row in df.iterrows():
        if row["separate_file"] == 1:
            dataframes[row["element_name"]] = main_df.copy(True)
            dataframes_dict[row["element_name"]] = []
        if row["avoid"] == 1:
            avoid_list.append(row["element_name"])

    return avoid_list, dataframes, dataframes_dict
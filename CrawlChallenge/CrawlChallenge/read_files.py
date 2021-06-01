import pandas as pd
from urllib.parse import urlparse
# from collections import Counter


def read_csv():
    df = pd.read_csv("DataEngineer_CodeChallenge_Input.csv")
    return df


def edit_df_data():
    df = read_csv()
    groupCount = 1
    group = {}

    newDf = df.sort_values(["url"], ascending=True).reset_index(drop=True)
    newList = newDf["url"].values.tolist()
    filterDomain = [urlparse(eachUrl).netloc for eachUrl in newList]
    countDic = {i: filterDomain.count(
        i) for i in filterDomain if filterDomain.count(i) >= 1}

    for i in countDic:
        group[i] = groupCount
        groupCount += 1

    return newDf, group, countDic


def make_df():
    newDf, group, countDic = edit_df_data()
    myDF = pd.DataFrame(columns=["group", "domain", "url", "count"])

    for index, row in newDf.iterrows():
        domain = urlparse(row["url"]).netloc
        myDF.loc[index] = [group[domain], domain, row["url"], countDic[domain]]
    return myDF



def output_df():
    newDf, group, countDic = edit_df_data()
    myDF = pd.DataFrame(columns=["group", "domain", "url", "count"])

    for index, row in newDf.iterrows():
        domain = urlparse(row["url"]).netloc
        myDF.loc[index] = [group[domain], domain, row["url"], countDic[domain]]
    myDF.to_csv("rebuild_data.csv")

output_df()



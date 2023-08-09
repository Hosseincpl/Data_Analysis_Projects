import pandas as pd

# Remove unnecessary row from WPP2022.xlsx and save as csv file
df_in = pd.read_excel("WPP2022.xlsx",sheet_name="Estimates")
df = df_in.drop([x for x in range(0,15)],axis=0).reset_index(drop=True)
df.columns = df.iloc[0]
df = df.drop([0], axis=0).drop(["Index"],axis=1).reset_index(drop=True)
df.rename(columns = {'Region, subregion, country or area *':'Country Name',"Year":"year"}, inplace = True)
df.to_csv("WPP2022.csv",header=True)

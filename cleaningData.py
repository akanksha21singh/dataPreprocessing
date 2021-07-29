import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt


from pandas.io.formats.format import CategoricalFormatter



dfRead = pd.read_csv("D:/UserData/z004ccdd/Documents/Python Scripts/test.csv")
#print(dfRead.head())
#print(dfRead.info())

#removing rows 
# for i in dfRead.index:
#     if(dfRead.loc[i,"age"]>60):
#         dfRead.drop(i,inplace=True)
# print(dfRead)

#splitting a col based on a character 
# dfRead[['countrycode','phonenumber']] = dfRead['countrycode_phonenumber'].str.split('_',expand=True)
# print(dfRead)

#removing columns
# to_drop = ["countrycode_phonenumber"]
# dfRead.drop(to_drop, inplace=True, axis=1)
# print(dfRead)

#filling missing values
#dfRead["address"].fillna(method='ffill',inplace=True,limit=1)
#dfRead["address"].fillna("enclave",inplace=True)

#removing unwanteds

#dfRead["address"]=dfRead["address"].str.replace(";","")
#dfRead["age"]=dfRead["age"].str.replace(";","").str.replace(":","").astype(int)

#readability
# dfRead['gender']=dfRead['gender'].astype("category")
# print(dfRead.info())
# dfRead['gender'].cat.rename_categories(new_categories={'M': 'Male', 'F': 'Female', 'U': 'Unknown'},
#                                     inplace=True)

#Filter specific columns based on their names
#dfRead = dfRead.filter(regex='july')

#visualising missing data
colours = ['#000099', '#ffff00']
sns.heatmap(dfRead.isnull(), cmap=sns.color_palette(colours))
plt.show()
#print(dfRead)



# -*- coding: utf-8 -*-
"""
Spyder Editor
Made by dnitecki
This is a temporary script file.
"""
import os
import pandas as pd
from pandas import ExcelWriter
cwd = os.path.abspath(r'C:\Users\dnitecki\Desktop\PM Sort')
files = os.listdir(cwd)
path = r'C:\Users\dnitecki\Desktop\PM Sort'
def highlight_cols(x):
    #df1[['Actuals']] = 'background-color: yellow'
    #if x['Actuals']:
    return 'background-color: yellow'
    

#Indirect Projects Files
df = pd.DataFrame()
for file in files:
    if file.startswith('Indirect'):
        df=df.append(pd.read_excel(path+'\\'+ file, header = 4),ignore_index=True)
        df=df[~df['Project Number'].isin(['Grand Total'])]
        print(file)
print(df)   
df.to_excel(r'C:\Users\dnitecki\Desktop\PM Sort\(Indirect) Projects Merge.xlsx', index=False)
print('done')

#PM Project Performance Files
df1 = pd.DataFrame()
for file in files:
    if file.startswith('PM'):
        df1=df1.append(pd.read_excel(path+'\\'+ file, header = 6),ignore_index=True)
        df1=df1[~df1['Project Number'].isin(['Grand Total'])]
        df1.fillna(0, inplace=True)
        actuals = df1['Billed to Date Revenue'] + df1['WIP (Unbilled)']
        df1['Actuals'] = actuals
        new = df1['Actuals']
        df1.drop(labels=['Actuals'], axis=1, inplace = True)
        df1.insert(5, 'Actuals', new)
        #df1['Actuals'].style.apply(highlight_cols, axis = None)
       
        #df1['Actuals'].set_properties(**{'background-color':"yellow"})
        print(file)

print(df1)
with ExcelWriter(r'C:\Users\dnitecki\Desktop\PM Sort\(PM) Projects Performance Merge.xlsx') as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)
    workbook = writer.book
    format_yellow= workbook.add_format()
    format_yellow.set_bg_color('yellow')
    worksheet=writer.sheets['Sheet1']
    worksheet.conditional_format('F2:F362',{"type":"text", 'criteria':'containing','value':"",'format': format_yellow})

#df1.style.applymap(highlight_cols).to_excel(r'V:\1755\administration\Project Controls\48. IPS Cumulative Export\1755\Project Task Detail\Oracle\(PM) Projects Performance Merge.xlsx', engine='openpyxl',index=False)
print('done')




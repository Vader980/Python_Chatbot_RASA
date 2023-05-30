import numpy as np
import pandas as pd

excelFile = 'C://Users/ukmak/OneDrive/Desktop/NWU Documents/MODULES/Third Year/CMPG 313/Project/Project Files/AIPROJECTXLS.xls'
df = pd.read_excel(excelFile)
#print(df)

#print(df['Class Venue'].where(df['Course Name'] == 'CMPG 313'))
AIclass = df['Class Venue'].where(df['Course Name'] == 'CMPG 313')
print(AIclass.dropna())
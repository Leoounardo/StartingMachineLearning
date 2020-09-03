import pandas as pd

allSheets = []
seed = 2031

while seed <= 2061:
    plan = pd.read_excel(r'C:/Users/ileoo/Desktop/ia/beleza{}.xlsx'.format(seed))
    allSheets.append(plan)
    seed+=1

newDf = pd.concat(allSheets)
newDf.to_excel(r'C:\Users\ileoo\Desktop\ia\belezafinal.xlsx', index=False, header=True)

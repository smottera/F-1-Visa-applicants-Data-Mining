import pandas as pd
import numpy as np
from tabulate import tabulate

f = open("F1Visa_Database.txt",'r')

bigList = []
smallList= []
x = 0
for lines in f:

    if(lines != '~~~\n'):
        smallList.append(lines)
    else:
        bigList.append(smallList)
        smallList = []

#for items in bigList:
 #   print(items)

data = pd.DataFrame(bigList,columns=['Name','Nationality', 'VisaType', 'Consulate', 'InterviewDate','Status', 'SlipColor','FinalDecisionDate','ProcessingTime', 'PassportStatus', 'DocsReq', 'DocsSubmitted','SubmDate','MiscInfo', 'CaseEntryCreated', 'CaseLastUpdate'])
#print(data)

F1df = data[data['VisaType'].str.contains("F1")]

Approveddf = data[data['Status'].str.contains("Pending")]

F1Approved = pd.merge(F1df, Approveddf, how='inner')

print(tabulate(F1Approved , headers='keys', tablefmt='psql'))

f.close()

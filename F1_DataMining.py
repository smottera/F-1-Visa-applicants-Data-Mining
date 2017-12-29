import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


f = open("F1Visa_Database.txt",'a')


def appendToFile(caseID):
    URLink = "https://redbus2us.com/trackers/221g-tracker/?caseid="
    URLink += caseID
    res = requests.get(URLink)
    soup = BeautifulSoup(res.content, 'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))

    stringg = ""
    for items in (df[0][1][0:]):
       stringg = stringg + str(items) + "\n"
    stringg += '~~~'+'\n'
    f.write(stringg)


def getCaseID(pageNumber,IDList):
    URLink2 = "https://redbus2us.com/trackers/221g-tracker/?page="
    URLink2 += str(pageNumber)
    res2 = requests.get(URLink2)
    soup = BeautifulSoup(res2.content, 'lxml')
    soup.prettify()
    str1 = ""
    str1 += str(soup)
    caseIDs = re.findall(r'caseid=[0-9]*',str1,re.I)
    for elements in caseIDs:
        #print(elements[7:])
        IDList.append(elements[7:])
    return IDList


#Get List of Case IDs
bigList = []
for x in range(1,15):
    bigList = getCaseID(x,bigList)

#print(bigList)
print(len(bigList))

for caseNos in bigList:
    print(caseNos)
    appendToFile(caseNos)
f.close()
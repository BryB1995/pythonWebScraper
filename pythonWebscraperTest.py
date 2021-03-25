import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas

fieldNames = ['price_($)', 'Full_String', 'URL']

def fileWrite(price):
    num = re.findall('[0-9.]', price)
    print(num)
    priceStr = ''.join(num)
    formatCheck = re.match('\.', priceStr)
    if formatCheck:
        pass
    else:
        priceStr = priceStr + ".00"

    print(priceStr)
    tempData = [priceStr, price, url_to_parse]
    csvCheck = pandas.read_csv('pythonTest.csv')
    if csvCheck.empty == False:
        with open('pythonTest.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(tempData)

    else:
            with open('pythonTest.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fieldNames)
                writer.writerow(tempData)








url_to_parse = input("enter URL to parse: ")
response = requests.get(url_to_parse)
print(response)
soup = BeautifulSoup(response.text,'html.parser')
#TD: get text, then parse
resIDList = soup.find_all(id=(re.compile('.price.||price', re.IGNORECASE)))
realIDList = soup.find_all(['h1', 'h2', 'h3', 'div', 'span', 'li'])

if len(resIDList) > 0:
    for x in range(0, len(resIDList)):
        print(resIDList[x].text)
        fileWrite(resIDList[x].text)


if len(realIDList) > 0:
    for x in range(0, len(realIDList)):
        candidate = realIDList[x].text
        test = re.search("\$|cad|CAD|usd|USD", candidate)
        if test is not None:
            print(test.string)
            fileWrite(test.string)




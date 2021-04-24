import csv
import requests
from bs4 import BeautifulSoup as bS


def main():
    
    keyw = input("Enter 3 or more words about what you need help with (separate using , or spaces > ").upper()

    if ',' in keyw:
        keyw = keyw.split(',')
    else: keyw = keyw.split(' ')
    
    if len(keyw)<3:
        print("Insufficient inputs, please enter 3 OR MORE keywords :) ")
        main()
    
    url = "https://www.thelivelovelaughfoundation.org/find-help/helplines"
    
    headerS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    page = requests.get(url, headers = headerS)
    soup = bS(page.content , 'html.parser')
    
    
    description = soup.find_all(class_="fullDesc")
    
    freq = {}
    orgNo = 0
    tempMain = {}

    for thisOrg in list(description):
        j = str(thisOrg.get_text)
        j = j.upper()
        j = j.replace(',','')
        j = j.replace('.','')
        j = j.replace('-','')        
        j = j.split(' ')
        
        for word in keyw:
            f = 0
            for checkHere in j:
                if word==checkHere:
                    f+=1
            freq[word]=f
            
        
        temp = freq.values()
        totalFreq = sum(temp)
        
        tempMain[orgNo] = totalFreq   
                
        orgNo+=1
        
    
    thisOrder = {k: v for k, v in sorted(tempMain.items(), key = lambda item: item[1])}
    myNGOs = [0]*2
    
    t = list(thisOrder.keys())
   
    myNGOs[0] = t[-1]
    myNGOs[1] = t[-2]
    
    
    with open('C:\\Users\\10aru\\Desktop\\Mindfully\\numbers.csv',encoding='latin-1') as f:
        numbers = list(csv.reader(f))
    
    print("\nHere's the help you needed - ")
    print(f'1 -  {numbers[myNGOs[0]][0].strip()}')
    print(f'2 -  {numbers[myNGOs[1]][0].strip()}')
    
    

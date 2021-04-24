import requests
from bs4 import BeautifulSoup as bS
import random as r

def main():
    url = input("Enter the URL - ")
    #url = "https://www.keepinspiring.me/quotes-about-happiness/"
    
    headerS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}
    page = requests.get(url, headers = headerS)
    soup = bS(page.content , 'html.parser')
    #print(soup.prettify())
    quotes = []
    for i in soup.find_all(class_="author-quotes"):
        quotes.append(i.get_text())
    f = open("happyQuotes.txt" ,"w" , encoding="utf-8")
    for quote in quotes:
        f.write(quote+"\n")
    f.close()
    
    
def todaysQuote():
    q = []
    n = 0
    f = open("happyQuotes.txt" , "r" , encoding="utf-8")
    for i in range(126):
        thisOne = f.readline()
        if len(thisOne)>150:
            continue
        else:
            q.append(thisOne)
            n+=1
        
    theChosenOne = q[r.randint(0,n)]
    
    return theChosenOne

if __name__ == "__main__":
    main()
else:
    todaysQuote()
    
    
    
    
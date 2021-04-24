from datetime import *
import speech_recognition as sr   
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import matplotlib.pyplot as plt
import os
import sys
import quotes as q
import m4aTowav as mw
import gettingHelp as gH

def writeToTextFile(y, d, mth, hr, minu):
    
    f = open("forGraph.txt" , mode="a" , encoding="utf-8")
    y = round(y*100 , 3)
    stamp = d + mth + "@" + hr + minu
    f.write(str(y)+","+stamp+"\n")
            
    f.close()
    print ("Recorded in a text file!\nExcellent work with the journalling!")
    
def speechrecog(AF):
   
    r = sr.Recognizer()    
    with sr.AudioFile(AF) as src: 
       audio = r.record(src) 
    
    print("Converting your beautiful voice note to text...")
    global S
    S = r.recognize_google(audio) 
    global Day, Month, Hour, Minute
    Day =  str(datetime.now().day) 
    Month = str(datetime.now().month)
    Hour = str(datetime.now().hour)
    Minute = str(datetime.now().minute)
    
    try:
        location = "C:\\Users\\10aru\\Desktop\\Mindfully\\myDiaryTEXTS\\"
        file = location + "E_for_" + Day + "-" + Month + "_at" + Hour + "-" + Minute 
        f = open(file + ".txt", "w") 
        f.write(S)
        f.close()
        return "Done!"
    except sr.UnknownValueError:
        return "ME NO KNOW WUT YOU SAY"
    except sr.RequestError:
        return "SYSTEM DOWN, SOWIE"
    
def sentimentAnalysis(data):
    Day =  str(datetime.now().day) 
    Month = str(datetime.now().month)
    Hour = str(datetime.now().hour)
    Minute = str(datetime.now().minute)
   # nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    ss = sia.polarity_scores(data);
   # print("------------------------------------------------------------------")
   # print("SENTENCE:" , data)
   # print("------------------------------------------------------------------")
        
   # print(ss['compound'])
    
    writeToTextFile(ss['compound'] , Day , Month , Hour , Minute)
    
def plotGraph():
    
    compounds = []
    when = []
    
        
    with open('forGraph.txt', mode='r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        n = 0
        for row in csvReader:
            compounds.append(row["compound"])
            when.append(row["stamp"])
            n += 1
       
            
    print(f'Here\'s your mood analysis for your last {n-1} entries...')
    
    compounds = [float(x) for x in compounds]
    when = [x[(x.index('@')+1):] for x in when]
    
    fig = plt.figure()
    fig.patch.set_facecolor('#222222')
    fig.patch.set_alpha(0.6)

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#222222')
    ax.patch.set_alpha(1.0)    
    plt.axis('off')
    plt.plot(when, compounds,"orange", linewidth=4.20)   
    plt.show()
    #Yea okay
def greeting():
    
    Hour = int(datetime.now().hour)
    
    if Hour<5 or Hour>=23:
        return "You should be sleeping"
    elif Hour>=5 and Hour<12:
        return "Happy morning"
    elif Hour>=12 and Hour<16:
        return "Good afternoon"
    else:
        return "Good evening"
    
def datetimePrettify(k):
    date = k[6:k.index('-')]
    tempDate = date
    date = list(date)
    if (date[0]=='1' and len(date)==2): add = "th"
    elif date[-1]=='1': add = "st"
    elif date[-1]=='2': add = "nd"
    elif date[-1]=='3': add = "rd"
    else : add = "th"            
            
    month = k[k.index('-')+1:k.index('_at')]
    if month == '1': month = "January"
    elif month == '2': month = "February"
    elif month == '3': month = "March"
    elif month == '4': month = "April"
    elif month == '5': month = "May"
    elif month == '6': month = "June"
    elif month == '7': month = "July"
    elif month == '8': month = "August"
    elif month == '9': month = "September"
    elif month == '10': month = "October"
    elif month == '11': month = "November"
    elif month == '12': month = "December"
        
    k = k[k.index('_at')+3:k.index('.')]
    
    hour = k[:k.index("-")]
    minu = k[k.index("-")+1:]
    if (len(minu) == 1):
        temp = "0"+ minu[0]
        minu = temp
    
    
    if (int(hour)>12):
        time = str(int(hour)-12)+ ":" + minu +" PM"
    else:
        time = hour + ":" + minu +" AM"
    
        
    return 'On ' + tempDate + add + " " + month + ', at ' + time


    
def previewPlus():
    
    print("\nHere are your older entries - \n")
    location = "C:\\Users\\10aru\\Desktop\\Mindfully\\myDiaryTEXTS\\"
    i = 1 
    for (dirpath, dirnames, filenames) in os.walk(location):
        for k in filenames:
            title = datetimePrettify(k)
            whichFile = location + k
            f = open(whichFile, "r")
            text = list(f.read())
            temp = text
            text = text[:60]
            print(str(i) + ") " + title + "\n" + ''.join(text) + "...\n")
            i+=1
    
    ch1 = (input("Want to see the files? Y/N > ")).upper()
    if ch1 == 'Y':        
        ch = int(input("Enter the entry number of the entry you want to visit > "))
        if (ch <= i):
            os.startfile(location+filenames[ch-1])
        else:
            print("Invalid Input!") 
    elif ch1 == 'N':
        pass
    else:
        print("Invalid Input!")
        
def newTextEntry():
    
    Day =  str(datetime.now().day) 
    Month = str(datetime.now().month)
    Hour = str(datetime.now().hour)
    Minute = str(datetime.now().minute)
    
    
    location = "C:\\Users\\10aru\\Desktop\\Mindfully\\myDiaryTEXTS\\"
    file = location + "E_for_" + Day + "-" + Month + "_at" + Hour + "-" + Minute + ".txt"
    f = open(file,"w")
    os.startfile(file)
    f.close()
    
    ch = input("Enter D when done > ").upper()
    
    if ch=='D':            
        f2 = open(file,"r")
        data = f2.read()
        sentimentAnalysis(data)
        f2.close()

    
    
    

def main():
    print("\tWhat do you want to do now?\n\t1. Make a new entry\n\t2. Go to older entries\n\t3. Get help")
    print("or - Enter Z to exit Mindfully")
    ch = input("ENTER 1/2/3/Z > ")
    if ch=='1':
        fileName = mw.changeOneFile()
        if fileName != 0:            
            print(speechrecog(fileName))
            sentimentAnalysis(S)
        else:
            ch = input("Want to make a text entry? Y/N > ").upper()
            if ch=='Y':
                newTextEntry()
            else:
                print("You've been living Mindfully for so long now, don't give up :'(")        
        main()
        
        
    elif ch=='2':
        plotGraph()
        previewPlus()
        main()
        
    elif ch=='3':
        gH.main()
        main()
    
    elif ch=='z' or ch=='Z':
        print("Bye-bye, see you soon!")
        sys.exit()
            
    else:
        print("Invalid Input!")       
        main()
        
    
if __name__ == "__main__":
    greetThis = greeting()
    print(greetThis+", person!")

    print(q.todaysQuote()) 
    
    main()
    
    
    
    

from selenium import webdriver
from bs4 import BeautifulSoup
import nltk
import re
import time

#create function scrape that can be imported
def scrape(links, save):
    PATH = "C://Program Files (x86)//chromedriver.exe" #specifiy webdriver path
    report = []
    for z in range(len(links)):
        content1 = [] #create content concerning the good news about the stock
        content2 = [] #create content concerning the bad news about the stock
        content3 = [] #create content concerning the statistics of the stock
        website = [] #website title list
        driver = webdriver.Chrome(PATH)
        driver.get(links[z])
        htmlSource = driver.page_source
        #print(htmlSource)
        
        soup = BeautifulSoup(htmlSource, 'html.parser') #use beautiful soup to parse html
        #print(soup)
        #print(soup.select('p'))
        elems = soup.select('p') #get p tags
        text = []
        for i in range(len(elems)):
            text.append(elems[i].getText()) #get the text from the p tags
        #print(text)
        #print(visible_text)
        text = " ".join(text) #join text with a space
        
        a_list = nltk.tokenize.sent_tokenize(text) #seperates the text into specific sentences
        
        #print(a_list)
        #print("___________________")
        
        #cleanse of periods and that bad stuff
        
        for i in range(len(a_list)):
            line = a_list[i] #gets one line from the list
            #print(line)
            newline = ""
            for char in line: 
                if char not in ".?\|/!-":
                    newline = newline + char #cleanses periods and other stuff
            a_list[i] = newline
            newline = ""
        
        #print("new alist, ", a_list)
        
        goodstuff = ["save", "soar", "increase", "up", "profitable", "growth"] #list of good stuff to scrape
        
        badstuff = ["poor", "bad", "decrease", "plummet", "debt", "hit"] #list of bad stuff to scrape
        
        #print("_______________________________________________________________")
        
        for i in range(len(a_list)):
            text_to_split = a_list[i]
            words = text_to_split.split()
            #print(words)
            for k in range(len(words)):
                if words[k] in goodstuff:
                    #print(a_list[i])
                    if "sign up" in a_list or "Sign up" in a_list or "Log in" in a_list or "log in" in a_list:
                            #print("SIGN UP")
                            continue
                    else:
                        content1.append(a_list[i])
                if words[k] in badstuff:
                    #print(a_list[i])
                    if "sign up" in a_list or "Sign up" in a_list or "Log in" in a_list or "log in" in a_list:
                            #print("SIGN UP")
                            continue
                    else:
                        content2.append(a_list[i])                    
        
        #print("_________________________________")
        for i in range(len(a_list)):
            if len(re.findall(r"(\+*|\-*)(\d+\.*\d*\%)", a_list[i])) != 0:
                #print(a_list[i])
                content3.append(a_list[i])
        website = [content1, content2, content3]
        report.append(website)
    
    data = []
    website_num = 0
    for website in report:
        website_num += 1
        data.append((f"Website {website_num}: {links[website_num-1]}\n"))
        for content_count in range(len(website)):
            if content_count == 0:
                data.append(f"\nGood Stuff\n\n")      
            if content_count == 1:
                data.append(f"\n\nBad Stuff\n\n")                     
            if content_count == 2:
                data.append(f"\n\nStatistics\n\n")        
            for line in website[content_count]:
                data.append(f"{line}")                
        data.append(f"\n\n")
    


    if save != '':
        to_open = save + 'stock_news.txt'
        dataFILE = open(to_open, 'w')
        website_num = 0
        for website in report:
            website_num += 1
            dataFILE.write(f"Website {website_num}\n")
            for content_count in range(len(website)):
                if content_count == 0:
                    dataFILE.write(f"\nGood Stuff\n\n")      
                if content_count == 1:
                    dataFILE.write(f"\n\nBad Stuff\n\n")                     
                if content_count == 2:
                    dataFILE.write(f"\n\nStatistics\n\n")        
                for line in website[content_count]:
                    dataFILE.write(f"{line}")                
            dataFILE.write(f"\n\n")
        dataFILE.close()
    time.sleep(1)


    return data


#test    
#l=["https://www.cnbc.com/2021/12/29/stocks-making-the-biggest-moves-premarket-cal-maine-tesla-alibaba-and-others.html"]

#scrape(l)
from django.shortcuts import render

# Create your views here.

from googlesearch import search   
from stockscraper import scraper
# to search 



def index(request):
    if request.method == "POST":
        keyword = request.POST["keyword"]
        save = request.POST["path"]
        numlinks = int(request.POST["numlinks"])
        links = []
        query = keyword + "news"
        for j in search(query, tld="co.in", num=numlinks, stop=2, pause=2): 
            links.append(j) 

        data = scraper.scrape(links, save) 
        return render(request, "stockscraper/done.html",{
            "keyword": keyword,
            "data": data,
        })
    else: 
        return render(request, "stockscraper/index.html")
    

ICS final project

This program encompasses three things that I've learned this year: Django, webscraping, and graph theory. 
The Django program is an airpot that employs user authentication, models, and POST methods. 
My webscraper scrapes html tags from a google search query, then seperates the scraped text into three 
distinct parts - good news concerning the stock, bad news and statistics (using regular expression). 
Finally, my graph theory problem uses classes, as well as the BFS algorithm to solve a CMIMC contest problem.

To use the program
Install git if you haven't already

Install packages:
Go onto the command line
--> pip install selenium
--> pip install beautifulsoup4
--> python -m pip install Django
--> pip install nltk
--> pip install numpy
--> pip install regex

Install the correct chromewebdriver (same version as your chrome, a different version will not work):
https://chromedriver.chromium.org/downloads

Change the file path of the Chrome webdriver in airport\stockscraper\scraper.py
i.e. PATH = "C://Program Files (x86)//chromedriver.exe"

--> cd /the/file/path/you/want/the/django/program/in
--> git clone https://github.com/Zli123123/Zhenhao_ICS3UFinal.git 
This will clone the github code in the path you specified

Go onto the command line and enter the django manage.py location which is the directory you cloned the program in
with /airport at the end
--> cd /where/the/program/is/located/airport

Create a superuser account to access models:
--> python manage.py createsuperuser 

type a valid username and password

run the program: 
--> python manage.py migrate
--> python manage.py runserver

Copy the local host into your web browser. 

Add model data such as flights, passengers and other users via admin:
http://127.0.0.1:8000/admin/

Now try the program! 

To login: 
http://127.0.0.1:8000/users/login

Already logged in:
http://127.0.0.1:8000/users

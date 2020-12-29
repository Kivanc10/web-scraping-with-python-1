# web-scraping-with-python-1

This mini python project's purpose was make web scraping to obtain clear data. This project contain two sub-projects. 

First, I have used to `https://store.steampowered.com/search/?specials=1` to retrieve top games datas.Such as game's name,price etc.

Second , I have visited `https://www.python.org/jobs/` to obtain new jobs datas. Wanted position , location , posted time etc.

## Getting Started
* As you seen at below , these photos belong to result of my projects. I stored them in dataframe objects.
* I'll explain , how to I achieved to retrieve and prettify data.

|         Top 40 Games in Steam    | Whole Job Offers in Python.org |
|----------------------------------|--------------------------------|
| <img src="/img/games_table.png"> | <img src="/img/jobs_table.png">|

|              Top 40 Games in Steam Visualizing                    |
|-------------------------------------------------------------------|
|  <img src="/img/film.png">                                        |


## Prerequisites
* `Requests`

* `bs4 from BeautifulSoup`

* `pandas`

* `matplotlib.pyplot`

* `seaborn`

## Installing

You should have libraries which reside at above . If you dont have them , you should install them to use program.
#### At first , python should be already installed in your device , if it is not , you should install python.

* Open command prompt and write `python`
    * if you see `Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32` something like your device has already has python.
    * if you see `Python is not recognized as an internal or external command, operable program or batch file.` something like, you should install python. You can download <a href="https://www.python.org/downloads/">here</a>


#### Then , you should make control whether has pip3 or not. To verify whether pip was installed:
 * open cmd and enter `pip -V`.
 
      * if you see `pip 19.2.3 from c:\python27\lib\site-packages\pip (python 2.7)` something like.It means , you had pip3 already.You can pass run section.
    
      * if you see `pip is not recognized as an internal or external command,Operable program or batch file` something like. You does not have pip3. You should install them.
    
         * Open command prompt and write `python get-pip.py` . Thanks to it , you will download get-pip.py
           
         * Then , verify to pip with `pip -V`.
           
         * Take advantages of latest facilities of python , write `python -m pip install --upgrade pip`
 
#### Install necessary libraries to run program
* `pip3 install requests`
* `pip3 install pandas`
* `pip install matplotlib`
* `pip3 install seaborn`
* `pip install lxml`

## Running the tests
* Open an editor like anaconda or visual studio and run the file.

#### Coding style tests

* At first , I defined variable variable of url.It store web site's url. 
* Then I made request to web server thanks to request module. After I made control to whether connect correctly or not. If code is 200 , it means process has been succesful.
* After that , I parsed and prettify html code that taken from web server with bs4 and store them in variable called soup.
* At last , I extracted pieces of informatin that I want from parsed code. As sample,I extract name of games. At below.
```
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://store.steampowered.com/search/?specials=1"


r = requests.get(url)

print(r.status_code)
soup = bs(r.content,"lxml")

games = soup.find_all("div",attrs={"class":"responsive_search_name_combined"})

for game in games:
    title = game.find("span",attrs={"class":"title"}).text
    print(title)
```


* Sample result of web scraping-1


![output_1](https://user-images.githubusercontent.com/51750773/103285674-de44e300-49ef-11eb-8213-d29f783079b0.png)




* If Multi-page exist , what will we doing

![Ekran Görüntüsü (135)](https://user-images.githubusercontent.com/51750773/103286750-fcabde00-49f1-11eb-9891-4015d04b73c6.png)

We should be write a python bot.The bot should be stroll each page and collect each's data.To do , we have to detect number of links. 
At below I detected them in variable called `pages `. -2 means , I extracted previous and next link from whole links.(code is reside at the below)




```
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import pandas as pd

url = "https://www.python.org/jobs/"

r = requests.get(url)

print(r.status_code)

soup = BeautifulSoup(r.content,"lxml")

pages = len(soup.find("ul",attrs={"class":"pagination"}).find_all("li")) - 2

df = pd.DataFrame(columns=["position","location","job_type","posted_time"])
count = 0

for page in range(1,pages+1): 
    pageRequests = requests.get("https://www.python.org/jobs/?page=" + str(page))
    print(pageRequests.url)
    page_soup = BeautifulSoup(pageRequests.content,"lxml")
    jobs = page_soup.find("div",attrs={"class","row"}).ol.find_all("li")
    for job in jobs:
        position = job.h2.find("a").text
        print(position)
```

The python bot , made request each pages.

![Ekran Görüntüsü (136)](https://user-images.githubusercontent.com/51750773/103287052-92476d80-49f2-11eb-893b-2ced7306eb38.png)

* As you see below , these are position of jobs that offered

![Ekran Görüntüsü (138)](https://user-images.githubusercontent.com/51750773/103287386-742e3d00-49f3-11eb-8288-7802a620857e.png)


           

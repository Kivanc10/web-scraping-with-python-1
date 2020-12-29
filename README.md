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


## Prerequisites
* `Requests`

* `bs4 from BeautifulSoup`

* `pandas`

* `matplotlib.pyplot`

* `seaborn`

## Installing

You should have libraries which reside at above . If you dont have them , you should install them to use program.
* Open command prompt and write `python`
    * if you see `Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32` something like your device has already has python.
    * if you see `Python is not recognized as an internal or external command, operable program or batch file.` something like, you should install python. You can download <a href="https://www.python.org/downloads/">here</a>

At first , python should be already installed in your device , if it is not , you should install python.


At first , you should make control whether has pip3 or not. To verify whether pip was installed:
 * open cmd and enter `pip -V`.
    * if you see `pip 19.2.3 from c:\python27\lib\site-packages\pip (python 2.7)` something like.It means , you had pip3 already.You can pass run section.
    * if you see `pip is not recognized as an internal or external command,Operable program or batch file` something like. You does not have pip3. You should install them.



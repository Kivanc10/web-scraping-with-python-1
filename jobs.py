# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:15:16 2020

@author: Kivanc
"""

#%%
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
    page_soup = BeautifulSoup(pageRequests.content,"lxml")
    #print(pageRequests.url)
    jobs = page_soup.find("div",attrs={"class","row"}).ol.find_all("li")
    # I have been retrieve all data , then I will try to catch the detail of jobs
    for job in jobs:
        position = job.h2.find("a").text
        location = job.find("span",attrs={"class":"listing-company-name"}).br.find_next().text
        job_type = job.find("span",attrs={"class":"listing-job-type"}).text
        posted_time = job.find("span",attrs={"listing-posted"}).time.text
        df.loc[count] = [position,location,job_type,posted_time]
        count+=1
#%%     
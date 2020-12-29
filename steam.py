# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:12:58 2020

@author: Kivanc
"""

#%%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://store.steampowered.com/search/?specials=1"


r = requests.get(url)

soup = bs(r.content,"lxml")

games = soup.find_all("div",attrs={"class":"responsive_search_name_combined"})

dict_games = dict()

df = pd.DataFrame(columns=["Game","Release Date","Price"])

count=0

for game in games:
    title = game.find("span",attrs={"class":"title"}).text
    release_date = game.find("div",attrs={"class","col search_released responsive_secondrow"}).text
    dict_games[title] = release_date
    price = game.select("div.col.search_price.discounted.responsive_secondrow")
    if price == []:
        price = "Free"
        continue
    else:
        price = price[0].find_next().find_next().find_next().next
    df.loc[count] = [title,release_date,price]
    count+=1

#df.to_csv("games.csv",sep="\t", encoding='utf-8')
#%% visualization
print(df.head())
print(df.info())
# necessary changes
df["Price"] = df["Price"].apply(lambda x : x.replace("TL",""))
df["Price"] = df["Price"].apply(lambda x : x.replace(",","."))
df["Price"] = df["Price"].apply(lambda x : float(x))

#%%
new_index = df["Price"].sort_values(ascending=False).index.values
new_df = df.reindex(new_index)

plt.figure(figsize=(15,10))
sns.barplot(x=new_df["Game"],y=new_df["Price"])
plt.xticks(rotation=90)
plt.xlabel("Games")
plt.ylabel("Price (TL)")
plt.title("Some Games which Has Discount in Steam")
plt.show()
#%%

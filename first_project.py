import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

#database space
conn=sqlite3.connect('database.db')

c=conn.cursor()
# create table in database
c.execute(''' CREATE TABLE Chops (title TEXT, ingrediant TEXT, rating TEXT )''')

#task is to scrape the url below and return igredients, titles and rating

url='https://www.allrecipes.com/recipes/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Alt-Svc':'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
    'Cache-Control':'no-cache, must-revalidate',
    'Content-Type':'image/gif',
    }

contents=requests.get(url, headers=headers)
print(contents.status_code)
soup=BeautifulSoup(contents.text, 'html.parser')

data=soup.find_all('a', class_='comp mntl-card-list-items mntl-document-card mntl-card card card--no-image',href=True)
store={}
store_1=[]
df=pd.DataFrame(columns=['title',"ingrediant",'rating'])
for link in data:
    
    url_2 =link['href']
    article=requests.get(url_2, headers=headers)
    soup_article=BeautifulSoup(article.content, 'html.parser')

    title=soup_article.find('h1',class_='article-heading type--lion').get_text().strip()
    ingrediant=soup_article.find('ul',class_='mntl-structured-ingredients__list').get_text().strip().replace('\n\n\n', " ,")
    rating=soup_article.find('div',class_="comp mntl-recipe-review-bar__rating mntl-text-block type--squirrel-bold")
    if rating is not None:
        rating=soup_article.find('div',class_="comp mntl-recipe-review-bar__rating mntl-text-block type--squirrel-bold").get_text()
    #rating=rating_1.findChildren('span', class_='ratings-histogram__average-text')

    c.execute(''' INSERT INTO Chops VALUES(?,?,?) ''',(title,ingrediant,rating))

    conn.commit() #comment after first run
    #extra option to load to Dataframe
    
    store={
        'title':title,
        'ingrediant':ingrediant,
        'rating':rating
    }
    lenght=len(df)
    df.loc[lenght]=store
    store_1.append(store)

c.execute(''' SELECT * from Chops ''')
display=c.fetchall()

print(display)
conn.close()
#df.to_csv("scrapped", index=False)
print("finished")






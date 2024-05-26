import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://markets.ft.com/data/currencies"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

data=requests.get(url,headers=headers)

print(data.status_code)


soup=BeautifulSoup(data.text, 'html.parser')

# get table tag from html data
table=soup.find('tbody')

table_row=table.find_all('tr')

data=[]
for row in table_row:
    row_data=[]
    for cell in row:
        row_data.append(cell.text)
    data.append(row_data)

#create a dataframe
df=pd.DataFrame(data)

df.to_csv('try_data', index=False)

print(df)


#looping throught the data


import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.investing.com/equities/apple-computer-inc-historical-data"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

data=requests.get(url,headers=headers)

print(data.status_code)
soup=BeautifulSoup(data.text, 'html.parser')
# get table tag from html data
table=soup.find('table',class_="freeze-column-w-1 w-full overflow-x-auto text-xs leading-4")

# trying to pull th from the table
table_head=table.find_all('th')
#looping through the head

table_title=[title.text for title in table_head]

df=pd.DataFrame(columns=table_title)
# getting data to fil in
column_data=table.find_all('tr')

for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_data=[data.text for data in row_data]

    #print(individual_data)
    lenght=len(df)
    df.loc[lenght]=individual_data

print(df['Price'])



#looping through the text
# data=[]
# for row in table_row:
#     row_data=[]
#     for cell in row:
#         row_data.append(cell.text)
#     data.append(row_data)
# #create a dataframe
# df=pd.DataFrame(data)
# table_head= df[0].tolist()
# df=df[2:]

# df.columns=table_head

# print(df.head())

#df=pd.DataFrame(columns=['Date','Price','Open','High','Low','Vol','Change'])
# col=row.find_all('td')
#     if len(col)!= 0:
#         df['Date']=col[0].text
#         df['Price']=col[1]
#         df['Open']=col[2]
#         df['High']=col[3]
#         df['Low']=col[4]
#         df['Vol']=col[5]
#         df['Change']=col[6]
#     print(df.head(5))

#looping throught the data
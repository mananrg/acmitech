import pandas as pd
import re
#file=open("My Activity.html","r")
#str_buff=file.read()

with open('My Activity.html', 'r') as f:
        file_content = f.read()
#print(str_buff)
#str_buff="Searched for  How to download google7 Oct 2002"
pattern=re.compile(r'<div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Searched for......ef="https://www.google.com/search\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\'\"\[\]\{\}\,\-\_\+\=\|\<\s]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\+\=\|\s]+)</a><br>(\d+\s...\s\d+)')
#\<a href="https://www.google.com/search\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\'\"\[\]\{\}\,\-\_\+\=\|\<\s]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\+\=\|\<\s]+)</a><br>(\d+\s...\s\d+)
#print(pattern)
    #phone=re.search(r'\d\s\w\w\w\s\d\d\d\d',x)
print(type(file_content))
#x=str(str_buff)
results=pattern.findall(file_content)
print("*************************************************************")
#print(type(results))
df = pd.DataFrame(results,columns=['Title','Timestamp'])
df.set_index('Timestamp',inplace=True)
#print(df)
for index,row in df.iterrows():
    print(row['Title'])
print("*************************************************************")
f.close()

'''
import re
import codecs
from bs4 import BeautifulSoup

f=codecs.open("My Activity.html", 'r', 'utf-8')
soup= BeautifulSoup(f.read(),'lxml')
#print(soup)

li=[]
for div in soup.findAll("div", {"class": "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"}):
    x=div.get_text()
    li.append(x)
    pattern=re.compile(r"Searched for (.+)([\d]+ ... ....)")
    phone=str(x)
    li.append(pattern.findall(phone))
    phone[0]=phone[0].encode("ascii","ignore")
    #print(phone)
print("***************************************************")
print(phone)
print("***************************************************")


for i in li:
    print(i)
    print(type(i))
    phone=re.findall(r'Searched for (.+)(\d ... ....)',i)
    print(phone)

'''

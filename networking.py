import requests
from bs4 import BeautifulSoup
url="https://www.bostonindia.in/products/networking/default.aspx?show=100&page="
a=0
for page in range(1,7):
    r=requests.get(url + str(page))
    serv=r.content
    soup=BeautifulSoup(serv,'html.parser')
    data=soup.find_all("div", { "class" : "row product-list-item" })
    for inp in data:
        a=a+1
        typee1=inp.find("div",{"class" : "text-muted"}).text
        typee=typee1.split(' ')
        provider=typee[0].split("\n")
        print( a,"=", "https:"+inp.img['src'].strip(), "=",inp.img['alt'],"=", provider[1].strip())
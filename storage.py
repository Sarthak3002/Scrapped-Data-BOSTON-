import requests
from bs4 import BeautifulSoup
url="https://www.bostonindia.in/products/storage/default.aspx?show=100&page="
a=0
for page in range(1,3):
    r=requests.get(url + str(page))
    serv=r.content
    soup=BeautifulSoup(serv,'html.parser')
    data=soup.find_all("div", { "class" : "row product-list-item" })
    for inp in data:
        a=a+1
        typee1=inp.find("div",{"class" : "text-muted"}).text
        info=inp.find_all("div",{"class" : "col-md-4"})
        typee=typee1.split(' ')
        provider=typee[0].split("\n")
        print( a,"=", "https:"+inp.img['src'].strip(), "=",inp.img['alt'].strip(),"=", provider[1].strip(),"=",info[0].text.strip(),"=",info[1].text.strip(),"=",info[2].text.strip() )



        



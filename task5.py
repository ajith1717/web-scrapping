from task4 import *
from pprint import pprint
a=requests.get(" https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(a.text,"html.parser")
table=soup.find("tbody")
table_row=table.find_all('tr')
url_list=[]
for i in table_row:
	table_col=i.find("td",class_="titleColumn")
	url_=table_col.find("a")
	url=" https://www.imdb.com"+url_["href"]
	url_list.append(url)
	# print(url_list)

z=[]
w=1
for i in url_list:
	print(w)
	w=w+1
	e=movie_de(i)
	z.append(e)	
print(z)
details=json.dumps(z)
file=open ("250.json","w+")
file.write(details)
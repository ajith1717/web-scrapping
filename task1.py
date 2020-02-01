import os,json
from bs4 import BeautifulSoup
if os.path.exists("ajith.json"):
	with open ("ajith.json","r") as files:
		a=json.load(files)
		b=json.loads(a)
	print(b)

else:
	a=requests.get(" https://www.imdb.com/india/top-rated-indian-movies/")
	print(a)
	# print(a.text)	
	soup=BeautifulSoup(a.text,"html.parser")
	table=soup.find("tbody")
	table_row=table.find_all('tr')
	movie=[]
	year_=[]
	for i in table_row:
		film_dic={}
		table_col=i.find("td",class_="titleColumn")
		dot=table_col.text.split(".")
		# print(dot[0]
		film_dic['Name']=table_col.find("a").text
		film_dic['year']=table_col.find("span").text.strip("(").strip(")")
		table_rat=i.find("td",class_="ratingColumn imdbRating")
		film_dic["ratings"]=table_rat.find("strong").text
		film_dic["position"]=dot[0].strip("\n").strip()
		url_=table_col.find("a")
		url=" https://www.imdb.com"+url_["href"]
		film_dic["url"]=url
		# print(film_dic)
		movie.append(film_dic)
	pprint.pprint(movie)
	print("else")
		# print(table_a.text)
	with open ("ajith.json","w") as file:
		b=json.dumps(movie)
		c=json.dump(b,file)			
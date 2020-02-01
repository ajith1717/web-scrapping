import os,json,requests
from bs4 import BeautifulSoup
from pprint import pprint
# if os.path.exists("ajith1.json"):
# 	with open ("ajith1.json","r") as file:
# 		a=json.load(file)
# 		b=json.loads(a)
# 	print(b)
		
# else:
def movie_de(i):
	# print(i)
	a=requests.get(i)
	print(a)
	soup=BeautifulSoup(a.text,"html.parser")
	movie={}
	m=soup.find("h1").text
	# pprint(m)
# 	nam=soup.find("div",class_="title_wrapper")
# 	name=nam.find("h1").text
	z=m.replace("\xa0"," ")
	name1="" 
	for i in z:
		if i=="(":
			break
		else:
			name1=name1+i
	movie["name"]=name1			
	die=soup.find("div",class_="credit_summary_item")
	d=[]
	na=die.find_all("a")
	for i in na:
		d.append(i.text)
	movie["director"]=d	
	
	
	cou=soup.find_all("div",class_="txt-block")
	c=[]
	for i in cou:
		if "Country" in i.text:
			movie["country"]=i.find("a").text
		if "Language" in i.text:
			lan=i.find_all("a")
			for j in lan:
				c.append(j.text)
	movie['Language']=c
	post=soup.find("div",class_="poster")
	movie["poster"]=post.find("img")["src"]		
	movie["bio"]=soup.find("div",class_="summary_text").text.strip("\n")
	genre=soup.find_all("div",class_="see-more inline canwrap")
	a=[]
	for j in genre:
		if "Genres" in j.find("h4").text:
			gen=j.find_all("a")
			for i in gen:
				a.append(i.text)
	movie["genre"]=a	
	time=soup.find_all("div",class_="txt-block")
	for i in time:
		if "Runtime" in i.text:
			movie["time"]=i.find("time").text
	return(movie)   

# movie_de(i)	 

#    #task 5##
# a=requests.get(" https://www.imdb.com/india/top-rated-indian-movies/")
# soup=BeautifulSoup(a.text,"html.parser")
# table=soup.find("tbody")
# table_row=table.find_all('tr')
# url_list=[]
# for i in table_row:
# 	table_col=i.find("td",class_="titleColumn")
# 	url_=table_col.find("a")
# 	url=" https://www.imdb.com"+url_["href"]
# 	url_list.append(url)
# 	# print(url_list)
# y=0	
# for i in url_list:
# 	y=y+1        
# 	# print(i)                                     #task5
# 	movie_de(i)
# 	if y==10:
# 		break			

# with open ("ajith1.json","w+") as file:
# 	b=json.dumps(movie)
# 	c=json.dump(b,file)			
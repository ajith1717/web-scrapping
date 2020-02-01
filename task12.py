# import requests,string,pprint
# from bs4 import BeautifulSoup
# a=requests.get("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")
# print(a)
# soup=BeautifulSoup(a.text,"html.parser")
# table=soup.find("table",class_="cast_list")
# # table_=table.find("tbody")
# # print(table_)
# table_row=table.find_all("tr",class_="odd")
# # print(table_row
# movie={}
# for i in table_row:
# 	name=i.find_all("td")
# 	a=0
# 	for j in name:
# 		n=j.find("a").text
# 		m=j.find("a")["href"]
# 		m=list(m)
# 		# print(m)
# 		o=m[6:15]
# 		l=""
# 		for i in o:
# 			l=l+i
# 		movie["name"]=n
# 		movie["1234"]=l
# 		a=a+1
# 		if a==2:
# 			break
# 	pprint.pprint(movie)
		
				
# 	# for j in 
# 	# for j in name:
# 	# 	if "name" in j:





#######################################
import string
a=[1,"a","ajith","zzz",2,0,190,"b","aaaa","qq"]
num=[]
abc=[]
for i in a:
	if i[0] in string.ascii_lowercase:
		abc.append(i)
	else:
		num.append(int(i))	
for i in num:
	for j in range(len(num)-1):
		if num[j]>num[j+1]:
			num[j],num[j+1]=num[j+1],num[j]

for i in abc:
	for j in range(len(abc)-1):
		if abc[j] > abc[j+1]:
			abc[j],abc[j+1]=abc[j+1],abc[j]
# print(num)
# print(abc)	
z=num+abc
print(z)

	# if len(i)==1:
	# 	print(b.index(i))

from task1 import b
from pprint import pprint
year=[]
de=[]
for i in b:
	if i["year"] not in year:
		year.append(i["year"])
for j in year:
	if int(j)%10==0:
		de.append(int(j))
	else:
		k=list(j)
		k[-1]='0'
		n=''.join(k)
		if int(n) not in de:
			de.append(int(n))
de.sort()
de=list(dict.fromkeys(de))		
pprint(de)	
year_={}
for i in de:
	year_list=[]
	for j in range(int(i),int(i)+10):
		for k in b:
			if str(j) in k["year"]:
				year_list.append(k)
		year_[i]=year_list
pprint(year_)
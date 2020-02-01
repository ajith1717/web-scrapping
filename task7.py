import json

with open('250.json','r+') as files:
	loader=json.load(files)
	director=[]
for i in loader:
	director.append(i["director"])
# print(language)

director1=[]
for j in director:
	if type(j)==list:
		for k in j:
			director1.append(k)
	else:
		director1.append(j)

dict1={}
for i in director1:
	if i not in dict1:
		dict1[i]=1
	else:
		dict1[i]+=1
print(dict1)

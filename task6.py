import json

with open('250.json','r+') as files:
	loader=json.load(files)
	language=[]
for i in loader:
	language.append(i["Language"])
# print(language)

languages=[]
for j in language:
	if type(j)==list:
		for k in j:
			languages.append(k)
	else:
		languages.append(j)

dict1={}
for i in languages:
	if i not in dict1:
		dict1[i]=1
	else:
		dict1[i]+=1
print(dict1)

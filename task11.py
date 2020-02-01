import json,pprint

with open('250.json','r+') as files:
	loader=json.load(files)
	genres=[]
for i in loader:
	genres.append(i["genre"])
# print(language)

genre=[]
for j in genres:
	if type(j)==list:
		for k in j:
			genre.append(k)
g={i:genre.count(i) for i in genre}
pprint.pprint(g)
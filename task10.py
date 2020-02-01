import json,pprint
with open('250.json','r+') as files:
	loader=json.load(files)
	director=[]
	for i in loader:
		director.append(i["director"])
	director1=[]	
	for j in director:
		if type(j)==list:
			for k in j:
				director1.append(k)
		else:
			director1.append(j)

	a=set(director1)
	print(a)
	movie={}
	for i in a:
		language=[]
		for j in loader:
			if i in j["director"]:
				if type(j["Language"])==list:
					for k in j["Language"]:
						language.append(k)
				b={l:language.count(l)for l in language}		

				# language.append(j["Language"])
				# print(j["Language"])
		movie[i]=b
	pprint.pprint(movie)


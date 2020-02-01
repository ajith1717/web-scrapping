import json
import string
from task1 import b
for i in b:
	# print(i["url"])
	b="tt"
	for j in i["url"]:
	    if j in string.digits:
	        b+=j
	# print(b)

	with open('250.json','r+') as files:
		loader=json.load(files)
		for k in loader:
			q=json.dumps(k)
			a=open(b+".json","w+")
			a.write(q)
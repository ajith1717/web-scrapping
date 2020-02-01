 from task1 import b
from pprint import pprint
a={}
for i in b:
	if i["year"] not in a:
		a[i["year"]]=[]
		a[i["year"]].append(i)
	else:
		a[i["year"]].append(i)
pprint(a)

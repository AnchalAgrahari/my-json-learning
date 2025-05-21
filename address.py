Dictionary={}
Dictionary['Anchal']={
	'name': 'Anchal',
	'DOB': '12 sept 2004',
	'phone' : '232435456'
}
print(" ")
Book={}
Book['Deepti']={
	'name': 'Deepti',
	'DOB': '26 aug 2004',
	'phone' : '988975687'
}
import json
d = json.dumps(Dictionary)
print(d)
a = json.dumps(Book)
print(a)
import json
d = {}
d['people'] = []
d['people'].append({'Name':'Thiago', 'Surname':'Martinelli', 'sign':'Virgo'})
d['people'].append({'Name':'Paul', 'Surname':'Simmons', 'sign':'Taurus'})

with open('data.json', 'w') as f:
	json.dump(d,f)

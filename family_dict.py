my_family = { 'sister': { 'name': 'Jocelyn', 'age': (26) },
	'mother': { 'name': 'Julia', 'age': (63) },
	'father':{'name': 'John', 'age': (62)} }

for k, v in my_family.items():
	family_rel = k
	family_name = (v['name'])
	family_age = (v['age'])
	# print(k)
	# print(v['name'], v['age'])

	jg_family =  'my ' + k + ' is ' + family_name + ' and is ' + str(family_age) + ' years old.'
	print(jg_family)

	jg_family = ['{0}']


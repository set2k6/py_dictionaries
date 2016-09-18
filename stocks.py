stockDict = { 'GM': 'General Motors', 'CAT': 'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]

for p in purchases:
	print(p[1]*p[3])
	# company_ticker = p[0]
	# company_name = stockDict[company_ticker]

for k, v in stockDict.items():
	print(v)

# full_name = {"symbol " + k + "'s" + "full name is " + v for (k,v) in stockDict.items()}
# 	print(full_name)




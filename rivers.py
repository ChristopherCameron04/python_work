rivers ={
'nile': 'egypt',
'zambezi': 'africa',
'amazon': 'south america'}

for river, country in rivers.items():
    print("\nThe " + river.title() + " River runs through " + 
    country.title() + ".") 

for river in rivers:
    print("\n" + river)


for country in rivers.values():
    print("\n" + country)

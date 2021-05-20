cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
]

ctlist = [

]
ctdict = {

}

for dictionary in cities:
    if not dictionary['country'] in ctlist:
        ctlist.append(dictionary['country'])
    
    for country in ctlist:
        new_value = []
            value = {}
            value[c] =   
        while value !
        if country in dictionary.values():
            ctdict[country] = [v for v in dictionary.values()]
            del(ctdict[country][2])
            print(ctdict)
        else:
            print("NOT WORKING!!! 🥴")
        
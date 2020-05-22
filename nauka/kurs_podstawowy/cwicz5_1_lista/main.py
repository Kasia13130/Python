countries = ['FR', 'US', 'DE', 'RU']
print(countries[1])
countries[1] = 'GB'
countries.append('PL')
countries.insert(2, 'ES')
countries.remove('RU')
countries.sort()
countries.reverse()
print(countries.pop(2))
print(countries.index('PL'))
print(countries.count('DE'))


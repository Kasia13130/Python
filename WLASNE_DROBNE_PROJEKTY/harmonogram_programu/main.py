line2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
print(line2)
time2 = line2[line2.find(":")+2:]
print(time2)
tmp2 = line2[line2.find('"'):30]
print(tmp2)
print(tmp2 + "   " + time2)
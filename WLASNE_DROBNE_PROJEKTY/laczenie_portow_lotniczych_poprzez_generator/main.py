ports = ["WAW", "KRK", "GDN", "KTW", "WMI", "WRO", "POZ", "RZE", "SZZ",
         "LUZ", "BZG", "LCJ", "SZY", "IEG", "RDO"]

counter = 0
gen = ((s, e) for s in ports for e in ports)
for (s, e) in gen:
    counter += 1
    print(s, "-", e)
print(counter)
print("\n")

counter = 0
gen = ((s, e) for s in ports for e in ports if s != e)
for (s, e) in gen:
    counter += 1
    print(s, "-", e)
print(counter)
print("\n")

counter = 0
gen = ((s, e) for s in ports for e in ports if s < e)
for (s, e) in gen:
    counter += 1
    print(s, "-", e)
print(counter)

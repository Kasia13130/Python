ports = ["WAW", "KRK", "GDN", "KTW", "WMI", "WRO", "POZ", "RZE", "SZZ",
         "LUZ", "BZG", "LCJ", "SZY", "IEG", "RDO"]

start_end_port = [(s, e) for s in ports for e in ports]
print(start_end_port)
print(len(start_end_port))

start_end_port = [(s, e) for s in ports for e in ports if s != e]
print(start_end_port)
print(len(start_end_port))

start_end_port = [(s, e) for s in ports for e in ports if s < e]
print(start_end_port)
print(len(start_end_port))

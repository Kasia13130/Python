import os
import urllib.request

data_dir = r"D:\Dokumenty\Kasia\studia\phyton nauka\kurs udemy\srednio_zaawansowany\cwicz1_5_polecenie_else_w_petlach\cwiczenie"
pages = [{"name": "mobilo", "url": "http://www.mobilo24.eu/"},
         {"name": "nonexistent", "url": "http://abc.cde.fgh.ijk.pl/"},
         {"name": "kursy", "url": "http://www.kursyonline24.eu/"}
         ]

for page in pages:
    try:
        path = os.path.join(data_dir, page["name"] + ".html")
        #print(path)
        local_name = urllib.request.urlretrieve(page["url"], path)
        print("{} done".format(local_name))
    except:
        print("{} Www page not exist".format(local_name))
        break
else:
    print("Following www pages was created")


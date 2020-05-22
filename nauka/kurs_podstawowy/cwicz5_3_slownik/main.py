CountryLeaders = {"PL": "Duda", "US": "Trump"}

print(CountryLeaders["US"])
CountryLeaders["DE"] = "Merkel"
print(CountryLeaders.keys())
print(CountryLeaders.values())
print(CountryLeaders.items())
print(CountryLeaders.popitem())
print(CountryLeaders.setdefault("FR", "Marcon"))

print(CountryLeaders.get("RU"))

NewLeaders = {"RU": "Putin", "DE": "Schulz"}
print(NewLeaders)
CountryLeaders.update(NewLeaders)

print(CountryLeaders)
print("\n")

#cwiczenie
chanels = {"Google": 1480, "Email": 300, "Natural traffic": 440, "TV Spot": 700}
print(chanels)
print(chanels["Email"])

chanelsUpdate = {"Natural Traffic": 520, "News": 600}
print(chanelsUpdate)
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
chanels.pop("Email")
print(chanels)
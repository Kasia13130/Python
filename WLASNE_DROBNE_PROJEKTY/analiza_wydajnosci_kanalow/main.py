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
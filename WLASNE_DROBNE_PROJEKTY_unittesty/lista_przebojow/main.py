hitsTitles = ["Brothers in arms", "Bohemia Rapsody", "Stairway to heaven", "Riders on the storm", "Wish you were here"]
print(hitsTitles)

hitsTitles.insert(2, "Child in time")
hitsTitles.append("Again")
print(hitsTitles)

hitsTitles[3] = "Hotel California"
print(hitsTitles)

hitsTitles[0] = "The sound of silence"
print(hitsTitles)

print(hitsTitles.index("Hotel California"))

hitsTitles.remove("Hotel California")
print(hitsTitles)

hitsTitles[0] = "Enjoy the silence"
print(hitsTitles)

hitsToRead = hitsTitles.copy()
print(hitsToRead)

hitsToRead.reverse()
print(hitsToRead)

hitsToRead.sort()
print(hitsToRead)

hitsToRead.pop(0)
hitsToRead.pop(0)
print(hitsToRead)

additionalSongs = ["Nothing compares 2 U", "Wish you were here"]
print(additionalSongs)
hitsToRead.extend(additionalSongs)
print(hitsToRead)

print(hitsToRead.count("Wish you were here"))
print(hitsToRead.count("Riders on the storm"))

print(hitsToRead.clear())
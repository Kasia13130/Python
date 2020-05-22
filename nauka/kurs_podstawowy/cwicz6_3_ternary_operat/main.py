itRains = False

if itRains:
    print("we stay at home")
else:
    print("we go out")

print("\n")

print("we stay at home" if itRains else "we go out")

print("\n")

# cwiczenia
musclePain = True
fever = True
weakness = True
isMan = False

if musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")

print("\n")

if musclePain and fever and weakness:
    print("suspicion of ifluenza")
elif weakness and not (fever and musclePain):
    print("Just take a break")
else:
    print("You may be cold")

print("\n")

if (musclePain and fever and weakness) or (musclePain and fever and weakness) and isMan:
    print("suspicion of influenza")
elif weakness and not (fever and musclePain):
    print("Just take a rest")
else:
    print("You may be cold")

print("\n")

isCheckCompleted = True

print("Check is completed" if isCheckCompleted else "Check not done yet!")
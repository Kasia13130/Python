drive = 'D:\\'
# pamietac o podwojnym backslash '\\'
folder = 'podstawy\\cwiczenie6_string2\\'
file = 'main.py'
path = drive + folder + file
print(path)

justText = r"text with\nnewline"
# 'r' przed cudzyslowem powoduje, ze znaki specjalne nie beda odczytane, czyli tekst wyswietli sie w jednej lini
print(justText)

justText = "Mc Donald's"
print(justText)

justText = 'Mc Donald\'s'
# jesli nie damy podwojnego cudzyslowu to trzeba pamietac by dac backslash, spowoduje to poprawne wyswietlenie tekstu
print(justText)

line = 'He said "I like Python!"'
print(line)
print("\n")

firstName = "Kasia"
familyName = "Sowa"
lastName = "Mrugala"
name = firstName + " " + familyName + " " + lastName
print(name)
print("\n")

# moj zapis
music = "\"Universal Fanfare\" Jerry Goldsmith \n\"Happy Together\" Garry Bonner\n\"I'm a Man\" Steve Winwood"
print(music)
print("\n")

# inne mozliwosci wyswietlenia zmiennej music
music2 = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'

music = "\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I'm a Man\" Steve Winwood"
print(music2)

music3 = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
print(music3)


something = '(\(\ \n( -.-)\n0_(")(")'
print(something)



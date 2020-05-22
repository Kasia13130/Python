number = 1
previus_number = 0

while number < 50:
    print(number + previus_number)
    previus_number = number
    number = number + 1         # blad ktory wystapil to brak znaku =

print("\n")

text = ''
number = 10
condition = True

while condition:
    text += 'x'
    print(text)

    if len(text) > number:
        condition = False

# blad ktory wystapil to warunek if bedacy na poziomie petli while a nie na poziomie print, przez co warunek
# byl nie wykonywanay, a petla dalej sie wykonywala
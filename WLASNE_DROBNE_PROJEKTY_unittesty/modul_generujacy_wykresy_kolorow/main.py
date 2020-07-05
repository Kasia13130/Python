
def colours(colour_list, n):

    return colour_list[:n]


colour_list = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colour_list) + 1):
    print(colours(colour_list, i), id(colours(colour_list, i)))


print("\n")
text = '''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod 
        przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji 
        pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania 
        człowieka w imię postępu. Rządzi w niej prawo dżungli.'''

text = text.replace("(", "- ").replace(")", "")
print(text[13:69])

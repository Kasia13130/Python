import sys
line = input("Price of next curse: ")
filepath = input("Enter file name: ")

try:
    file = open(filepath, "w")
    file.write(line)
    file.close()
    value = int(line)
    print("The value saved in file is...", value)

except FileNotFoundError as e:
    print("Error opening file: ", filepath, e)
except ValueError as e:
    print("The value entered cannot be converted to a number: ", e)
except:
    print("Sorry - we have an error. Try again.", sys.exc_info()[0])
else:
    print("Actions completed successfully")
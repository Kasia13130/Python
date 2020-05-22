file_path = (r"D:\\Dokumenty\\Kasia\\studia\\phyton nauka\\kurs udemy\\podstawy\\cwicz10_4_odczyt_z_pliku\\orders.csv")

with open(file_path, "r") as file:
    for line in file:
        order = line.replace("\n", "").replace(";", "").split(",")

        if len(order) == 3:
            print("Order from drugstore '%s', item '%s' amount '%s'" % (order[0], order[1], order[2]))
        if len(order) != 3:
            print("Line %s malformed !!!" % (order))
print("\nData processing completed!")
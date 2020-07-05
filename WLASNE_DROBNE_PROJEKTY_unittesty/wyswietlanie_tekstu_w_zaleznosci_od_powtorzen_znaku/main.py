def show_progress(how_many, character="*"):
    print(character * how_many)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, "-")
show_progress(15, "+")

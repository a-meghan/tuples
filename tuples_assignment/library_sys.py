library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_new_books(new_book):
    if new_book not in library:
        library.append(new_book)
        print(f"Added '{new_book[0]}' by {new_book[1]} to our library.")
    else:
        print(f"We already have a copy of '{new_book[0]}' by {new_book[1]} in our library. Thanks!")

my_book_to_add = ("A Court of Thorns And Roses", "Sarah J Mass")
duplicate_test = ("A Court of Thorns And Roses", "Sarah J Mass")
add_new_books(my_book_to_add)
add_new_books(duplicate_test)
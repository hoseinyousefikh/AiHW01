books = {}

while True:
    command = input("Enter a command (add/search/show/exit): ")
    if command == "add":
        name = input("Enter the book name: ")
        author = input("Enter the author name: ")
        books[name] = author
        print("Book added successfully.")
    elif command == "search":
        name = input("Enter the book name: ")
        if name in books:
            print("Author:", books[name])
        else:
            print("This book is not in the library.")
    elif command == "show":
        if len(books) == 0:
            print("There are no books in the library.")
        else:
            print("Available books:")
            for name in books:
                print(name, "-", books[name])

    elif command == "exit":
        print("Program ended.")
        break
    else:
        print("Invalid command.")

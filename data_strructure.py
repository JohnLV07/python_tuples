#2. Python Data Structure Challenges in Real-World Scenarios

'''
Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library):

    
    title = input("Enter the name of the book: ")
    author = input("Enter the book's author name: ")
    book1 =  (title, author)
    if book1 not in library:
        library.append(book1)
        print("Book added succesfully!")
    else:
        print("Book already in library.")
    return library




while True:
    print("\nLibrary adder")
    print("\n1: Add new Book\n2: Exit")
    choice = input("select what you want to do: ")

    if choice == '1':
        
        add_book(library)
        print(library)

    elif choice == '2':
        print("Exiting the system.")
        break

    else:
        print("Invalid option please try again.")
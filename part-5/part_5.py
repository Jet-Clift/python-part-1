### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(books):
    title = input("\nWhat is the book's title?")
    author = input("Who is the author of the book?")
    try:
        year = int(input("What year was the book published?"))
    except:
        year = int(input("Only numbers are accepted here."))
    try:
        rating = float(input("What is the star rating (out of 5) that this book received?"))
    except:
        rating = float(input("Only numbers from 0 to 5 are accepted."))
    try:
        pages = int(input("How many pages are in this book?"))
    except:
        pages = int(input("Only numbers are allowed."))

    with open(books, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

# with open(books, "r") as f:
with open("library.txt", "r") as f:
    file = f.readlines()

    for line in file:
        title, author, year, rating, pages = line.split(", ")

        book_dictionary = {
           "title": title,
           "author": author,
           "year": int(year),
           "rating": float(rating),
           "pages": int(pages)
        }

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def get_books_as_list(books):
    book_list = []
    with open(books, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            book_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return book_list

def get_book_printed(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}")

def view_books(books):
    print("\nHere are all your books...\n")
    for book in get_books_as_list(books):
        get_book_printed(book)

def get_highest_rated_book(books):
    list = get_books_as_list(books)
    return max(list, key=lambda x: int(x["rating"]))


def menu(books):
    active = True

    while active:
        choice = input("Click 1 to add a book. Click 2 to see all books. Click 3 to exit the library. - ")

        active = True

        if choice == "1":
            books.append(create_new_book())
        elif choice == "2":
            print(books)
        elif choice == "3":
            print(f"\nYou have a total of {len(books)} books.\n")
        elif choice == "4":
            print(f"\nYour books have a total of {sum([x['pages'] for x in books])} pages!\n")
        elif choice == "4":
            print("\nHere is your highest rated book:")
            get_book_printed(get_highest_rated_book)
        elif choice == "5":
            print("\nGoodbye")
            active = False




if __name__ == "__main__":
    menu("library.txt")
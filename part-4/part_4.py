### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
#def create_new_book():
#    new_book_title = input("What is the book's title?")
#    new_book_author = input("Who is the author of the book?")
#    new_book_year = input("What year was the book published?")
#    new_book_rating = input("What is the star rating (out of 5) that this book received?")
#    new_book_pages = input("How many pages are in this book?")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
def create_new_book():
    new_book_title = input("What is the book's title?")
    new_book_author = input("Who is the author of the book?")
    new_book_year = int(input("What year was the book published?"))
    new_book_rating = float(input("What is the star rating (out of 5) that this book received?"))
    new_book_pages = int(input("How many pages are in this book?"))
### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
title = input("What is the book's title?")
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


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def menu(books):

     choice = input("Click 1 to add a book. Click 2 to see all books. Click 3 to exit the library. - ")

     if choice == "1":
         books.append(create_new_book())
     elif choice == "2":
         print(books)
     elif choice == "3":
         print("Goodbye")
         active = False

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

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
        elif choice == "5":
            print("\nGoodbye")
            active = False
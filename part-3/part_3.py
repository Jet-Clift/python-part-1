my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(my_book):
    book_string = f"The novel, {my_book["title"]}, written by {my_book["author"]}, was published in {my_book["year"]}, is {my_book["pages"]} pages long, and has a rating of {my_book["rating"]} out of 5."
    return book_string

print(book_parser(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(my_book):
    title = my_book["title"]
    return title
print(get_title(my_book))

def get_author(my_book):
    author = my_book["author"]
    return author
print(get_author(my_book))

def get_year(my_book):
    year = my_book["year"]
    return year
print(get_year(my_book))

def get_rating(my_book):
    rating = my_book["rating"]
    return rating
print(get_rating(my_book))

def get_pages(my_book):
    pages = my_book["pages"]
    return pages
print(get_pages(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def get_highest_rated_book(books):
    list = books
    return max(list, key=lambda x: int(x["rating"]))
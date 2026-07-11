#======================================== Library Management System ======================================#
def header_title(title):
    print("="*40)
    print(title.center(40))
    print('='*40)
    
books = []
#========================== 1. ADD BOOK =============================#
def add_book():
    header_title("1. ADD BOOK")
    while True:
        title = input("Enter Book Title: ").strip()
        if not title:
            print("Please Enter A Valid Title!")
            continue
        break

    while True:
        author_name = input("Enter Author Name: ").strip()
        if not author_name:
            print("Please Enter A Valid Name!")
            continue
        break

    while True:
        id_exists = False
        book_id = input("Enter Book ID: ").strip()
        for book in books:
            if book["book_id"].lower() == book_id.lower():
                id_exists = True
        if not id_exists:
            break
        else:
            print("The Book ID Already Exists. Please Enter a Unique Book ID.")
            continue

    book = {
        "title" : title,
        "author_name" : author_name,
        "book_id" : book_id,
        "status" : "Available"
    }
    books.append(book)
    print("✅ Book Added Successfully!")

#========================== 2. VIEW BOOKS =============================#
def view_books():
    header_title("2. VIEW BOOKS")
    count_book = 0
    if not books:
        print("The Are No Books.")
        return
    for book in books:
        count_book += 1
        print("-"*40)
        print(f"Book #{count_book}")
        print(f"Title     : {book['title']}")
        print(f"Author    : {book['author_name']}")
        print(f"Book ID   : {book['book_id']}")
        print(f"Status    : {book['status']}")
    print("-"*40)
    print(f"Total Books {count_book}")
    print("-"*40)

#========================== 3. SEARCH BOOK =============================#
def search_book():
    header_title("3. SEARCH BOOK")
    search = input("Pleae Enter The Book Title To Search: ").strip()
    searched_list = []
    for book in books:
        if book["title"].lower() == search.lower():
            searched_list.append(book)
    if not searched_list:
        print("No Book Found")
        return
    else:
        count_search = 0
        for book in searched_list:
            count_search += 1
            print("-"*40)
            print(f"Book #{count_search}")
            print(f"Title     : {book['title']}")
            print(f"Author    : {book['author_name']}")
            print(f"Book ID   : {book['book_id']}")
            print(f"Status    : {book['status']}")
        print("-"*40)
        print(f"Total Books {count_search}")
        print("-"*40)    


#========================== 4. BORROW BOOK =============================#
def borrow_book():
    header_title("4. BORROW BOOK")
    if not books:
        print("No Book Found.")
        return
    
    while True:
        title = input("Enter Book Title: ").strip()
        if not title:
            print("Please Enter A Valid Title!")
            continue
        break
    for book in books:
        if book["title"].lower() == title.lower():
            if book["status"] == "Available":
                print("Book Borrowed Susscessfully.")
                book["status"] = "Borrowed"
                break
            else :
                print("Book is already Borrowed.")
                return
        print("Book Not Found.")

#========================== 5. Return BOOK =============================#
def return_book():
    header_title("5. RETURN BOOK")
    if not books:
        print("No Book Found.")
        return
    
    while True:
        title = input("Enter Book Title: ").strip()
        if not title:
            print("Please Enter A Valid Title!")
            continue
        break
    for book in books:
        if book["title"].lower() == title.lower():
            if book["status"] == "Borrowed":
                print("Book Returned Susscessfully.")
                book["status"] = "Aailable"
                break
            else :
                print("Book is already Available.")
                return
        print("Book Not Found.")

#========================== Display Menu ===============================#
def dispaly_menu():
    header_title("Library Management System")
    print("1. ADD BOOK ")
    print("2. VIEW BOOK ")
    print("3. SEARCH BOOK ")
    print("4. BORROW BOOK ")
    print("5. RETURN BOOK ")
    print("6. EXIT ")

#========================== Run Program ===============================#
def run():
    while True:
        dispaly_menu()
        choice = int(input("Please Enter Your Choice: "))
        match choice:
            case 1:
                add_book()
            case 2:
                view_books()
            case 3:
                search_book()
            case 4:
                borrow_book()
            case 5:
                return_book()
            case 6:
                break
    print("*"*40)
    print("Thank You For Using Library Management System")

if __name__ == "__main__":
    run()
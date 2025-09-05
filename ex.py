import os

BOOK_FILE = "library.txt"
USER_FILE = "users.txt"

# ----------------- FILE HANDLING -------------------
def load_books():
    books = {}
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as f:
            for line in f:
                book_id, title, author, qty = line.strip().split("|")
                books[book_id] = {"title": title, "author": author, "quantity": int(qty)}
    return books

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        for book_id, details in books.items():
            f.write(f"{book_id}|{details['title']}|{details['author']}|{details['quantity']}\n")

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                uid, uname, pwd, role = line.strip().split("|")
                users[uid] = {"username": uname, "password": pwd, "role": role}
    return users

def save_users(users):
    with open(USER_FILE, "w") as f:
        for uid, details in users.items():
            f.write(f"{uid}|{details['username']}|{details['password']}|{details['role']}\n")

# ----------------- ADMIN FUNCTIONS -------------------
def add_book(books):
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("❌ Book ID already exists!")
        return
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    qty = int(input("Enter Quantity: "))
    books[book_id] = {"title": title, "author": author, "quantity": qty}
    save_books(books)
    print("✅ Book added successfully!")

def remove_book(books):
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        save_books(books)
        print("🗑️ Book removed successfully!")
    else:
        print("❌ Book not found.")

def view_all_books(books):
    if not books:
        print("📂 No books available.")
        return
    print("\n--- Library Books ---")
    print("{:<10} {:<30} {:<20} {:<5}".format("ID", "Title", "Author", "Qty"))
    for book_id, details in books.items():
        print("{:<10} {:<30} {:<20} {:<5}".format(
            book_id, details['title'], details['author'], details['quantity']
        ))

def view_all_users(users):
    print("\n--- Registered Users ---")
    print("{:<10} {:<15} {:<10}".format("User ID", "Username", "Role"))
    for uid, details in users.items():
        print("{:<10} {:<15} {:<10}".format(uid, details['username'], details['role']))

def search_book(books):
    keyword = input("Enter Book ID or Title to search: ").lower()
    found = False
    for book_id, details in books.items():
        if keyword in book_id.lower() or keyword in details['title'].lower():
            print(f"🔎 {book_id} - {details['title']} by {details['author']} (Qty: {details['quantity']})")
            found = True
    if not found:
        print("❌ Book not found.")

# ----------------- USER FUNCTIONS -------------------
def issue_book(books):
    book_id = input("Enter Book ID to issue: ")
    if book_id in books and books[book_id]["quantity"] > 0:
        books[book_id]["quantity"] -= 1
        save_books(books)
        print(f"📖 Book '{books[book_id]['title']}' issued successfully!")
    else:
        print("❌ Book not available.")

def return_book(books):
    book_id = input("Enter Book ID to return: ")
    if book_id in books:
        books[book_id]["quantity"] += 1
        save_books(books)
        print(f"📚 Book '{books[book_id]['title']}' returned successfully!")
    else:
        print("❌ Invalid Book ID.")

# ----------------- MENUS -------------------
def admin_panel(books, users):
    while True:
        print("\n===== Admin Panel =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. View All Users")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            view_all_users(users)
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")

def user_panel(books):
    while True:
        print("\n===== User Panel =====")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            issue_book(books)
        elif choice == "2":
            return_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

# ----------------- LOGIN SYSTEM -------------------
def login(users):
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")

    if uid in users and users[uid]["password"] == pwd:
        print(f"✅ Welcome {users[uid]['username']} ({users[uid]['role']})")
        return users[uid]["role"]
    else:
        print("❌ Invalid login!")
        return None

# ----------------- MAIN PROGRAM -------------------
def main():
    books = load_books()
    users = load_users()

    # Default admin if no users file exists
    if not users:
        users["admin"] = {"username": "admin", "password": "admin123", "role": "admin"}
        save_users(users)

    print("===== Library Management System =====")
    while True:
        role = login(users)
        if role == "admin":
            admin_panel(books, users)
        elif role == "user":
            user_panel(books)
        else:
            print("Try again...")

if __name__ == "__main__":

    main()
import os

BOOK_FILE = "library.txt"

# ----------------- FILE HANDLING -------------------
def load_books():
    books = {}
    if os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "r") as f:
            for line in f:
                book_id, title, author, qty = line.strip().split("|")
                books[book_id] = {"title": title, "author": author, "quantity": int(qty)}
    return books

def save_books(books):
    with open(BOOK_FILE, "w") as f:
        for book_id, details in books.items():
            f.write(f"{book_id}|{details['title']}|{details['author']}|{details['quantity']}\n")

# ----------------- ADMIN FUNCTIONS -------------------
def add_book(books):
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("❌ Book ID already exists!")
        return
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    qty = int(input("Enter Quantity: "))
    books[book_id] = {"title": title, "author": author, "quantity": qty}
    save_books(books)
    print("✅ Book added successfully!")

def remove_book(books):
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        save_books(books)
        print("🗑️ Book removed successfully!")
    else:
        print("❌ Book not found.")

def view_all_books(books):
    if not books:
        print("📂 No books available.")
        return
    print("\n--- Library Books ---")
    print("{:<10} {:<30} {:<20} {:<5}".format("ID", "Title", "Author", "Qty"))
    for book_id, details in books.items():
        print("{:<10} {:<30} {:<20} {:<5}".format(
            book_id, details['title'], details['author'], details['quantity']
        ))

def search_book(books):
    keyword = input("Enter Book ID or Title to search: ").lower()
    found = False
    for book_id, details in books.items():
        if keyword in book_id.lower() or keyword in details['title'].lower():
            print(f"🔎 {book_id} - {details['title']} by {details['author']} (Qty: {details['quantity']})")
            found = True
    if not found:
        print("❌ Book not found.")

# ----------------- USER FUNCTIONS -------------------
def issue_book(books):
    book_id = input("Enter Book ID to issue: ")
    if book_id in books and books[book_id]["quantity"] > 0:
        books[book_id]["quantity"] -= 1
        save_books(books)
        print(f"📖 Book '{books[book_id]['title']}' issued successfully!")
    else:
        print("❌ Book not available.")

def return_book(books):
    book_id = input("Enter Book ID to return: ")
    if book_id in books:
        books[book_id]["quantity"] += 1
        save_books(books)
        print(f"📚 Book '{books[book_id]['title']}' returned successfully!")
    else:
        print("❌ Invalid Book ID.")

# ----------------- MENUS -------------------
def admin_panel(books):
    while True:
        print("\n===== Admin Panel =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

def user_panel(books):
    while True:
        print("\n===== User Panel =====")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            issue_book(books)
        elif choice == "2":
            return_book(books)
        elif choice == "3":
            view_all_books(books)
        elif choice == "4":
            search_book(books)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

# ----------------- MAIN PROGRAM -------------------
def main():
    books = load_books()
    print("===== Library Management System =====")
    while True:
        role = input("\nAre you 'admin' or 'user'? (type exit to quit): ").lower()
        if role == "admin":
            admin_panel(books)
        elif role == "user":
            user_panel(books)
        elif role == "exit":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please type 'admin' or 'user'.")

if __name__ == "__main__":
    main()

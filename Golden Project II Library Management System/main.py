import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="5112",
  database="library"
)

# Function to add a new book to the library
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the book genre: ")
    year = input("Enter the published year: ")
    
    # Insert the new book into the library table
    cursor = db.cursor()
    sql = "INSERT INTO library (title, author, genre, published_year) VALUES (%s, %s, %s, %s)"
    val = (title, author, genre, year)
    cursor.execute(sql, val)
    db.commit()
    print("Book added successfully!")
    
# Function to search for books in the library
def search_books():
    keyword = input("Enter a keyword to search for: ")
    cursor = db.cursor()
    sql = "SELECT * FROM library WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s OR published_year LIKE %s"
    val = ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%')
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if results:
        print("Search results:")
        for result in results:
            print(result)
    else:
        print("No results found.")
    
# Function to update a book in the library
def update_book():
    book_id = input("Enter the ID of the book you want to update: ")
    title = input("Enter the new title (leave blank to keep the current title): ")
    author = input("Enter the new author (leave blank to keep the current author): ")
    genre = input("Enter the new genre (leave blank to keep the current genre): ")
    year = input("Enter the new published year (leave blank to keep the current year): ")
    
    # Update the book in the library table
    cursor = db.cursor()
    sql = "UPDATE library SET title=%s, author=%s, genre=%s, published_year=%s WHERE id=%s"
    val = (title, author, genre, year, book_id)
    cursor.execute(sql, val)
    db.commit()
    if cursor.rowcount > 0:
        print("Book updated successfully!")
    else:
        print("No book found with that ID.")
        
# Main loop
while True:
    print("Welcome to the library management system!")
    print("1. Add a new book")
    print("2. Search for books")
    print("3. Update a book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        search_books()
    elif choice == '3':
        update_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        
# Close the database connection
db.close()

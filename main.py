import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# Connect to the SQLite database
conn = sqlite3.connect('library2.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS books 
             (serial_no INTEGER PRIMARY KEY, book_id TEXT, book_name TEXT, book_author TEXT, copies INTEGER, year INTEGER)''')
conn.commit()

# Function to add a book
def add_book():
    if not all([book_id_entry.get(), book_name_entry.get(), book_author_entry.get(), copies_entry.get(),
                year_entry.get()]):
        messagebox.showerror("Error", "Please fill all fields")
        return
    book_id = book_id_entry.get()
    book_name = book_name_entry.get()
    book_author = book_author_entry.get()
    copies = copies_entry.get()
    year = year_entry.get()
    c.execute("INSERT INTO books (book_id, book_name, book_author, copies, year) VALUES (?, ?, ?, ?, ?)", (book_id, book_name, book_author, copies, year))
    conn.commit()
    messagebox.showinfo("Success", "Book added successfully")
    refresh_table()

    # Clear entry fields after adding the book
    book_id_entry.delete(0, tk.END)
    book_name_entry.delete(0, tk.END)
    book_author_entry.delete(0, tk.END)
    copies_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)


# Function to remove a book
def remove_book():
    book_id = book_id_remove_entry.get()

    # Confirm removal with user
    confirm = messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove the book with ID '{book_id}'?")

    if confirm:
        # Retrieve book details before removal
        c.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
        removed_book = c.fetchone()

        # Delete the book from the database
        c.execute("DELETE FROM books WHERE book_id=?", (book_id,))
        conn.commit()

        messagebox.showinfo("Success", "Book removed successfully")
        refresh_table()

        # Display details of the removed book
        messagebox.showinfo("Book Details",
                             f"Book ID: {removed_book[1]}\n"
                             f"Book Name: {removed_book[2]}\n"
                             f"Book Author: {removed_book[3]}\n"
                             f"Copies: {removed_book[4]}\n"
                             f"Year: {removed_book[5]}")
    else:
        messagebox.showinfo("Cancelled", "Removal cancelled")

# Function to refresh the table
def refresh_table():
    # Clear existing data in the table
    for row in books_treeview.get_children():
        books_treeview.delete(row)

    # Retrieve books from the database and insert them into the table
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        books_treeview.insert("", "end", values=book)

# GUI setup
root = tk.Tk()
root.title("Library Management System")

book_id_label = tk.Label(root, text="Book ID")
book_id_label.grid(row=0, column=0)
book_id_entry = tk.Entry(root)
book_id_entry.grid(row=0, column=1)

book_name_label = tk.Label(root, text="Book Name")
book_name_label.grid(row=1, column=0)
book_name_entry = tk.Entry(root)
book_name_entry.grid(row=1, column=1)

book_author_label = tk.Label(root, text="Book Author")
book_author_label.grid(row=2, column=0)
book_author_entry = tk.Entry(root)
book_author_entry.grid(row=2, column=1)

copies_label = tk.Label(root, text="Copies")
copies_label.grid(row=3, column=0)
copies_entry = tk.Entry(root)
copies_entry.grid(row=3, column=1)

year_label = tk.Label(root, text="Year")
year_label.grid(row=4, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=5, column=0, columnspan=2)

book_id_remove_label = tk.Label(root, text="Book ID to Remove")
book_id_remove_label.grid(row=6, column=0)
book_id_remove_entry = tk.Entry(root)
book_id_remove_entry.grid(row=6, column=1)

remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.grid(row=7, column=0, columnspan=2)

# Create Treeview widget for displaying books
books_treeview = ttk.Treeview(root, columns=("ID", "Book_ID", "Book_Name", "Book_Author", "Copies", "Year"), show="headings")
books_treeview.heading("ID", text="ID")
books_treeview.heading("Book_ID", text="Book_ID")
books_treeview.heading("Book_Name", text="Book_Name")
books_treeview.heading("Book_Author", text="Book_Author")
books_treeview.heading("Copies", text="Copies")
books_treeview.heading("Year", text="Year")
books_treeview.grid(row=8, column=0, columnspan=2)

refresh_table()
root.mainloop()

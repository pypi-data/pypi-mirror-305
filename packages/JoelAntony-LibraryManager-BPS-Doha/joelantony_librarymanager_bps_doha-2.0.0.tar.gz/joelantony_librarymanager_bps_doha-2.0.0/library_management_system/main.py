import json
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Load data from JSON files
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to JSON files
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

class Library:
    def __init__(self):
        self.books = load_data("books.json")
        self.users = load_data("users.json")

    def get_user_info(self, admission_number):
        return next((u for u in self.users if str(u.get("admission_number", "")) == admission_number), None)

    def add_book(self, title, author, isbn, genre):
        if not title or not author or not isbn or not genre:
            messagebox.showerror("Error", "All book details must be provided.")
            return
        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "available": True
        }
        self.books.append(book)
        save_data("books.json", self.books)
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")

    def issue_book(self, admission_number, book_title):
        user = self.get_user_info(admission_number)
        book = next((b for b in self.books if b["title"].lower() == book_title.lower() and b["available"]), None)
        if not user:
            messagebox.showerror("Error", "All details must be provided.")
            return
        if not book:
            messagebox.showerror("Error", "Book not available.")
            return

        user.setdefault("borrowed_books", []).append(book["title"])
        book["available"] = False
        save_data("users.json", self.users)
        save_data("books.json", self.books)
        messagebox.showinfo("Success", f"Book '{book_title}' issued to '{user['name']}'.")

    def return_book(self, admission_number, book_title):
        user = self.get_user_info(admission_number)
        book = next((b for b in self.books if b["title"].lower() == book_title.lower() and not b["available"]), None)
        if not user:
            messagebox.showerror("Error", "All details must be provided.")
            return
        borrowed_books_lower = [b.lower() for b in user.get("borrowed_books", [])]
        if not book or book_title.lower() not in borrowed_books_lower:
            messagebox.showerror("Error", "Book not borrowed by user.")
            return
        user["borrowed_books"].remove(next(b for b in user["borrowed_books"] if b.lower() == book_title.lower()))
        book["available"] = True
        save_data("users.json", self.users)
        save_data("books.json", self.books)
        messagebox.showinfo("Success", f"Book '{book_title}' returned by '{user['name']}'.")

    def check_library_status(self):
        total_books = len(self.books)
        available_books = len([b for b in self.books if b["available"]])
        borrowed_books = total_books - available_books
        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books
        }

class LibraryGUI:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Library Management System - Login")
        self.root.config(bg="#d1e7dd")
        self.root.resizable(False, False)
        
        tk.Label(root, text="Admin Login", font=("Arial", 16, "bold"), bg="#d1e7dd").pack(pady=20)
        tk.Label(root, text="Username:", bg="#d1e7dd").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password:", bg="#d1e7dd").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Login", command=self.check_login, bg="#198754", fg="white")
        self.login_button.pack(pady=15)
        
        self.root.bind("<Return>", lambda event: self.check_login())

    def check_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if username == "jo362" and password == "bpsdoha":
            self.show_welcome_screen()
        else:
            messagebox.showerror("Login Error", "Admin details are incorrect")

    def show_welcome_screen(self):
        self.root.withdraw()
        self.welcome_screen = tk.Toplevel(self.root)
        self.welcome_screen.geometry("600x500")
        self.welcome_screen.title("Welcome to BPS Doha, admin")
        self.welcome_screen.config(bg="#d1e7dd")
        self.welcome_screen.resizable(False,False)
        greeting = tk.Label(self.welcome_screen, text="", font=("Arial", 14, "bold"), bg="#d1e7dd", fg="#198754")
        greeting.pack(pady=20)
        welcome_message = f"Welcome to BPS Doha, admin. Good {self.get_greeting()}!"

        def animate_message(idx=0):
            greeting["text"] = welcome_message[:idx]
            if idx < len(welcome_message):
                self.welcome_screen.after(100, animate_message, idx + 1)

        animate_message()

        button_style = {'bg': '#198754', 'fg': 'white', 'font': ('Arial', 12, 'bold'), 'relief': 'flat'}
        tk.Button(self.welcome_screen, text="Register New Book", **button_style, command=self.show_register_book_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Student Details", **button_style, command=self.show_student_details_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Issue Book", **button_style, command=self.issue_book_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Return Book", **button_style, command=self.return_book_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Check Library Status", **button_style, command=self.check_library_status_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Available Books", **button_style, command=self.show_available_books_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Borrowed Books", **button_style, command=self.show_borrowed_books_window).pack(pady=5)
        tk.Button(self.welcome_screen, text="Logout", **button_style, command=self.logout).pack(pady=20)

    def get_greeting(self):
        current_hour = datetime.now().hour
        return "Morning" if 5 <= current_hour < 12 else "Afternoon" if 12 <= current_hour < 17 else "Evening"

    def logout(self):
        self.welcome_screen.destroy()  # Close the welcome screen
        self.root.deiconify()  # Show the login window again

    def show_register_book_window(self):
        window = tk.Toplevel(self.root)
        window.title("Register New Book")
        window.geometry("400x300")
        window.resizable(False, False)
        
        tk.Label(window, text="Title:", font=("Arial", 12)).pack(pady=5)
        title_entry = tk.Entry(window, width=30)
        title_entry.pack(pady=5)

        tk.Label(window, text="Author:", font=("Arial", 12)).pack(pady=5)
        author_entry = tk.Entry(window, width=30)
        author_entry.pack(pady=5)

        tk.Label(window, text="ISBN:", font=("Arial", 12)).pack(pady=5)
        isbn_entry = tk.Entry(window, width=30)
        isbn_entry.pack(pady=5)

        tk.Label(window, text="Genre:", font=("Arial", 12)).pack(pady=5)
        genre_entry = tk.Entry(window, width=30)
        genre_entry.pack(pady=5)

        tk.Button(window, text="Register Book", command=lambda: self.library.add_book(title_entry.get(), author_entry.get(), isbn_entry.get(), genre_entry.get()), bg="#198754", fg="white").pack(pady=10)

    def show_student_details_window(self):
        window = tk.Toplevel(self.root)
        window.title("Student Details")
        window.geometry("400x300")
        window.resizable(False, False)
        tk.Label(window, text="Enter student admission number:", font=("Arial", 12)).pack(pady=10)
        self.student_search_entry = tk.Entry(window, width=30)
        self.student_search_entry.pack(pady=5)

        tk.Button(window, text="Search", command=self.fetch_student_details, bg="#198754", fg="white").pack(pady=10)
        self.student_info_display = tk.Text(window, height=10, width=40, wrap="word")
        self.student_info_display.pack(pady=10)
        self.student_info_display.config(state="disabled")

    def fetch_student_details(self):
        admission_number = self.student_search_entry.get().strip()
        if not admission_number:
            messagebox.showwarning("Input Error", "Please enter an admission number.")
            return
        
        user = self.library.get_user_info(admission_number)

        self.student_info_display.config(state="normal")
        self.student_info_display.delete("1.0", tk.END)
        
        if user:
            fines = f"${user['fine_amount']}" if 'fine_amount' in user else "0"
            borrowed_books = "\n".join(user.get("borrowed_books", [])) or "No books borrowed."
            details = f"Name: {user['name']}\nAdmission Number: {user['admission_number']}\nBorrowed Books:\n{borrowed_books}\nFine: {fines}"
            self.student_info_display.insert(tk.END, details)
        else:
            self.student_info_display.insert(tk.END, "Student not found.")
        
        self.student_info_display.config(state="disabled")

    def show_borrowed_books_window(self):
        window = tk.Toplevel(self.root)
        window.title("Borrowed Books")
        window.geometry("800x500")
        window.resizable(False, False)
        borrowed_books = [(u['name'], u['admission_number'], b) for u in self.library.users for b in u.get("borrowed_books", [])]

        tree = ttk.Treeview(window, columns=("Student Name", "Admission No.", "Book Title"), show="headings")
        tree.heading("Student Name", text="Student Name")
        tree.heading("Admission No.", text="Admission No.")
        tree.heading("Book Title", text="Book Title")
        tree.pack(fill="both", expand=True)

        for record in borrowed_books:
            tree.insert("", tk.END, values=record)

    def issue_book_window(self):
        window = tk.Toplevel(self.root)
        window.title("Issue Book")
        window.geometry("400x200")
        window.resizable(False, False)
        
        tk.Label(window, text="Admn No:", font=("Arial", 12)).pack(pady=5)
        user_id_entry = tk.Entry(window, width=30)
        user_id_entry.pack(pady=5)

        tk.Label(window, text="Book Title:", font=("Arial", 12)).pack(pady=5)
        book_title_entry = tk.Entry(window, width=30)
        book_title_entry.pack(pady=5)

        tk.Button(window, text="Issue Book", command=lambda: self.library.issue_book(user_id_entry.get(), book_title_entry.get()), bg="#198754", fg="white").pack(pady=10)

    def return_book_window(self):
        window = tk.Toplevel(self.root)
        window.title("Return Book")
        window.geometry("400x200")
        window.resizable(False, False)
        
        tk.Label(window, text="Admn No:", font=("Arial", 12)).pack(pady=5)
        user_id_entry = tk.Entry(window, width=30)
        user_id_entry.pack(pady=5)

        tk.Label(window, text="Book Title:", font=("Arial", 12)).pack(pady=5)
        book_title_entry = tk.Entry(window, width=30)
        book_title_entry.pack(pady=5)

        tk.Button(window, text="Return Book", command=lambda: self.library.return_book(user_id_entry.get(), book_title_entry.get()), bg="#198754", fg="white").pack(pady=10)

    def check_library_status_window(self):
        status = self.library.check_library_status()
        messagebox.showinfo("Library Status", f"Total Books: {status['total_books']}\nAvailable Books: {status['available_books']}\nBorrowed Books: {status['borrowed_books']}")

    def show_available_books_window(self):
        window = tk.Toplevel(self.root)
        window.title("Available Books")
        window.geometry("400x300")
        tree = ttk.Treeview(window, columns=("Title", "Author"), show="headings")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.column("Title", anchor="w", width=200)
        tree.column("Author", anchor="w", width=150)
        for book in self.library.books:
            if book["available"]:
                tree.insert("", "end", values=(book["title"], book["author"]))

        tree.pack(fill="both", expand=True)

# Run the GUI
if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    LibraryGUI(root, library)
    root.mainloop()

# Library Management System (BPS)

The Library Management System (BPS) is a simple yet effective tool designed to help manage a library's book inventory and user interactions. This application provides a user-friendly graphical interface, allowing librarians to efficiently register new books, issue books to students, and manage returns.

## Features

- **User Authentication**: Secure admin login to access the library management features.
- **Book Management**: Register new books with details like title, author, ISBN, and genre.
- **Issue and Return Books**: Issue books to students and manage the return process.
- **Student Details**: Retrieve student information based on their admission number.
- **Library Status**: Check the total number of books, available books, and borrowed books.
- **Available and Borrowed Books**: View lists of available books and borrowed books.

## Technologies Used

- Python 3.6 or higher
- Tkinter for the GUI
- JSON for data storage

## Installation

You can install the package using pip:

pip install LibraryManagementSystem


## Usage

To run the application, execute the following command:


python -m library_management_system.main


## Data Storage

The application uses JSON files (`books.json` and `users.json`) to store information about books and users. Ensure these files are present in the same directory as the script for the application to function correctly.

## Author

**Joel Varghese Antony**  
joelantony30101@gmail.com

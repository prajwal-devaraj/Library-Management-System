# Library Management System

This project is a **Library Management System** that helps manage the operation of a library. It allows administrators to manage books, users, and transactions such as issuing and returning books. The system aims to streamline the library process, making it more efficient and user-friendly.

📂 **GitHub Repository:** [Library Management System](https://github.com/prajwaldevaraj-2001/Library-Management-System)

---

## 🚀 Overview

The system is designed to:
- Manage **books** and **users**.
- Perform **issue** and **return** of books.
- Track **due dates** and **fines** for late returns.

## 🔹 Key Features:
- **Book Management**: Add, update, and remove books in the library.
- **User Management**: Add, update, and remove users.
- **Issue & Return Books**: Manage book issuance and returns with due dates.
- **Fines**: Track fines for late book returns.
- **Search Functionality**: Search for books and users easily.
- **Admin Access**: Admin can perform all the actions in the system.

---

## 🛠️ Technologies Used

- **Backend**: Python
- **Frontend**: HTML, CSS (optional)
- **Database**: SQLite (local storage of books, users, and transactions)
- **Library**: Tkinter (for GUI)

---

## ⚙️ Installation & Setup
🔹 1. Clone the Repository</br>
git clone https://github.com/prajwaldevaraj-2001/Library-Management-System.git</br>
cd Library-Management-System</br>

🔹 2. Install Dependencies</br>
Make sure to install the required libraries before running the application:</br>
pip install -r requirements.txt</br>

🔹 3. Run the Application</br>
If you're running the system as a standalone Python application with a GUI:</br>
python main.py</br>
If you're using a web version with HTML, CSS, and JavaScript, you can serve the templates with Flask:</br>
flask run</br>

🔹 4. Access the System</br>
For the GUI version, it will open as a window on your desktop. For the web version, navigate to http://127.0.0.1:5000/ in your browser.

## 🔧 Usage
📌 Features in Action
1. Book Management
- Add New Book: Add a book to the library by providing details like title, author, genre, and quantity.
- View Books: Browse through the available books in the library.
- Delete/Update Book: Update or remove books from the library collection.
2. User Management
- Add New User: Register a new library member with details like name, email, and user type (student or staff).
- View Users: View and manage the list of library members.
3. Issue/Return Books
- Issue Book: Issue a book to a user. Track the due date and book status.
- Return Book: Return a book and calculate any fines for late returns.
4. Search Functionality
- Search for books and users with ease.

## 📊 Example Usage
After running the application:

- Book Management:
Open the Add Book section to add a new book.
Use the Search bar to find a book by title or author.
Click on a book to update or delete its information.

- User Management:
Go to the Add User page to register a new library user.
Search for users and view or edit their information.
Transactions:

- Issue a book to a user.
Track when the book is due for return and calculate fines based on the number of late days.

## 📝 Future Improvements
- ✅ Web Interface: Improve user experience by developing a web interface with Flask or Django.
- ✅ Advanced Features: Integrate barcode scanning for quick book check-ins and check-outs.
- ✅ Fine Calculation: Implement a more detailed fine system that accounts for overdue books and applies penalties based on duration.


## 📂 Project Structure

```plaintext
Library-Management-System/
│
├── assets/                       # Images, Icons, and other assets
│
├── src/                          # Source code files
│   ├── library.py                # Main logic for library operations
│   ├── user.py                   # User management logic
│   ├── book.py                   # Book management logic
│   └── transaction.py            # Transaction (issue/return) logic
│
├── templates/                    # HTML templates (if used for web)
│   ├── index.html                # Dashboard
│   ├── add_book.html             # Add new book page
│   └── add_user.html             # Add new user page
│
├── requirements.txt              # Python dependencies
├── README.md                     # Documentation
└── main.py                        # Entry point to run the system

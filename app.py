from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# MongoDB connection (update with your credentials)
MONGO_URI = "mongodb+srv://pkadam:piyushaK%400709@cluster0.1kt2x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client['library_management']  # Database name
books_collection = db['books']
borrowers_collection = db['borrowers']
transactions_collection = db['transactions']
issues_collection = db['issues']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Get counts of books, borrowers, and issued books
    books_count = books_collection.count_documents({})
    borrowers_count = borrowers_collection.count_documents({})
    issued_books_count = transactions_collection.count_documents({'status': 'issued'})
    return render_template('dashboard.html', books_count=books_count, borrowers_count=borrowers_count, issued_books_count=issued_books_count)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        copies = int(request.form['copies'])

        # Ensure book details are provided
        if title and author and isbn and copies > 0:
            book = {
                "title": title,
                "author": author,
                "isbn": isbn,
                "copies": copies
            }
            books_collection.insert_one(book)
            flash("Book added successfully!", "success")
        else:
            flash("All fields are required, and copies should be greater than 0.", "danger")
        return redirect(url_for('add_book'))
    return render_template('add_book.html')

@app.route('/view_books')
def view_books():
    books = books_collection.find()
    return render_template('view_books.html', books=books)

@app.route('/update_book/<isbn>', methods=['GET', 'POST'])
def update_book(isbn):
    book = books_collection.find_one({'isbn': isbn})
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        copies = int(request.form['copies'])

        if title and author and copies > 0:
            books_collection.update_one(
                {'isbn': isbn},
                {'$set': {'title': title, 'author': author, 'copies': copies}}
            )
            flash("Book updated successfully!", "success")
            return redirect(url_for('view_books'))
        else:
            flash("All fields are required and copies should be greater than 0.", "danger")
    
    return render_template('update_book.html', book=book)

@app.route('/delete_book/<isbn>', methods=['GET', 'POST'])
def delete_book(isbn):
    book = books_collection.find_one({'isbn': isbn})
    if request.method == 'POST':
        if book:
            books_collection.delete_one({'isbn': isbn})
            flash("Book deleted successfully!", "success")
            return redirect(url_for('view_books'))
        else:
            flash("Book not found.", "danger")
    return render_template('delete_book.html', book=book)

@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        borrower_name = request.form['borrower_name']
        
        # Find the book based on ISBN
        book = books_collection.find_one({'isbn': isbn})
        
        # Check if book exists and has copies available
        if book and book['copies'] > 0:
            # Update the book's copy count and record the transaction
            books_collection.update_one({'isbn': isbn}, {'$inc': {'copies': -1}})
            transaction = {
                "isbn": isbn,
                "borrower_name": borrower_name,
                "status": "issued"
            }
            transactions_collection.insert_one(transaction)
            flash("Book issued successfully!", "success")
        else:
            flash("Book unavailable or invalid ISBN.", "danger")
        return redirect(url_for('issue_book'))
    return render_template('issue_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        borrower_name = request.form['borrower_name']
        
        # Find the issued transaction to return
        transaction = transactions_collection.find_one({'isbn': isbn, 'borrower_name': borrower_name, 'status': 'issued'})
        
        # Check if the transaction exists and update accordingly
        if transaction:
            # Update book's copies and mark transaction as returned
            books_collection.update_one({'isbn': isbn}, {'$inc': {'copies': 1}})
            transactions_collection.update_one({'_id': transaction['_id']}, {'$set': {'status': 'returned'}})
            flash("Book returned successfully!", "success")
        else:
            flash("Invalid transaction details.", "danger")
        return redirect(url_for('return_book'))
    return render_template('return_book.html')

@app.route('/report_issue', methods=['GET', 'POST'])
def report_issue():
    if request.method == 'POST':
        book_id = request.form['book_id']
        issue_description = request.form['issue_description']

        if book_id and issue_description:
            issue = {
                "book_id": book_id,
                "issue_description": issue_description,
                "status": "reported"
            }
            issues_collection.insert_one(issue)
            flash("Issue reported successfully!", "success")
        else:
            flash("Please fill in all fields.", "danger")
        return redirect(url_for('report_issue'))
    return render_template('report_issue.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

books = []

# Home route
@app.route('/')
def home():
    return 'Welcome to the Library API!'

# Create a book (POST)
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Read all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Read a single book by ID (GET)
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Update a book by ID (PUT)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update(updated_book)
        return jsonify(book), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

# Delete a book by ID (DELETE)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

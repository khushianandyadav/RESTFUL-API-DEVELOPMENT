# RESTFUL-API-DEVELOPMENT
*COMPANY*: CODTECH IT SOLUTIONS
*NAME*: KHUSHI ANAND YADAV
*INTERN ID*: CT08GKA
*DOMAIN*: SOFTWARE DEVELOPMENT
*DURATION*: 4 WEEKS
*MENTOR*: NEELA SANTHOSH KUMAR

# DESCRIPTION

Designing a RESTful API for a library or inventory system involves implementing CRUD (Create, Read, Update, Delete) operations. Below is a description of the provided Python code, which uses the Flask web framework to build such an API.

The Flask library is imported to create the web application, along with request and jsonify for handling requests and responses in JSON format. The application is named app and initialized using Flask(__name__).

 Data Storage

An empty list named books is created to store book data. Each book is expected to be represented as a dictionary.

 Home Route

The home route (/) is defined to return a welcome message. This can be accessed via a simple GET request to the root URL:


@app.route(/)
def home():
    return 'Welcome to the Library API!'


 Create a Book (POST)

The add_book function allows users to add a new book to the library. It handles POST requests to the /books endpoint. The function retrieves the JSON data from the request, appends it to the books list, and returns the new book along with a 201 status code indicating successful creation:


@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

 Read All Books (GET)

The get_books function handles GET requests to the /books endpoint. It returns the entire list of books along with a 200 status code, indicating a successful operation:


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200


 Read a Single Book by ID (GET)

The get_book function retrieves a specific book by its ID. It handles GET requests to the /books/<int:book_id> endpoint. The function searches for the book in the books list by its id and returns it if found, along with a 200 status code. If the book is not found, it returns a 404 status code with a "Book not found" message:


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

 Update a Book by ID (PUT)

The update_book function updates the information of a specific book by its ID. It handles PUT requests to the /books/<int:book_id> endpoint. The function retrieves the updated book data from the request, finds the book in the `books` list, and updates it if found. If the book is not found, it returns a 404 status code with a "Book not found" message:


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update(updated_book)
        return jsonify(book), 200
    else:
        return jsonify({'message': 'Book not found'}), 404


 Delete a Book by ID (DELETE)

The delete_book function deletes a specific book by its ID. It handles DELETE requests to the /books/<int:book_id> endpoint. The function filters out the book with the matching id from the books list and returns a success message with a 200 status code:


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 200


 Running the Application

Finally, the application is run with debugging enabled:


if __name__ == '__main__':
    app.run(debug=True)


This API design enables users to interact with a library or inventory system, performing CRUD operations on books. Each endpoint is mapped to a specific HTTP method, ensuring a RESTful approach. The use of JSON for request and response bodies makes the API easy to integrate with various clients.


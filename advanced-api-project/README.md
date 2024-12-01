## API Endpoints

- `GET /api/books/`: List all books.
- `GET /api/books/<id>/`: Retrieve a single book by ID.
- `POST /api/books/create/`: Create a new book (requires authentication).
- `PUT /api/books/<id>/update/`: Update a book (requires authentication).
- `DELETE /api/books/<id>/delete/`: Delete a book (requires authentication).

## Permissions
- Authenticated users can create, update, or delete books.
- Unauthenticated users can only view books.

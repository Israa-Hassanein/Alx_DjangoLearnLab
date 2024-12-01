## API Endpoints

- `GET /api/books/`: List all books.
- `GET /api/books/<id>/`: Retrieve a single book by ID.
- `POST /api/books/create/`: Create a new book (requires authentication).
- `PUT /api/books/<id>/update/`: Update a book (requires authentication).
- `DELETE /api/books/<id>/delete/`: Delete a book (requires authentication).

## Permissions
- Authenticated users can create, update, or delete books.
- Unauthenticated users can only view books.

## API Endpoints

### Filtering, Searching, and Ordering

You can filter, search, and order books using the following query parameters:

- **Filtering**:
  - Filter by title: `/books/?title=<title>`
  - Filter by author: `/books/?author=<author>`
  - Filter by publication_year: `/books/?publication_year=<year>`

- **Searching**:
  - Search by title or author: `/books/?search=<query>`

- **Ordering**:
  - Order by title: `/books/?ordering=title`
  - Order by publication_year: `/books/?ordering=publication_year`
  - For descending order: prefix with `-`, e.g., `/books/?ordering=-publication_year`



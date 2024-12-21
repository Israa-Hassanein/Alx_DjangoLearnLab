# Django Social Media API

This project is a Django-based social media API that supports user registration and authentication. The project includes a custom user model with additional fields such as `bio`, `profile_picture`, and `followers`. It uses Django REST Framework (DRF) for handling API endpoints and token-based authentication.

---

## **Setup Process**

### **Step 1: Clone the Repository**
Clone the repository to your local machine:
```bash
git clone <repository_url>
cd social_media_api
```

### **Step 2: Create a Virtual Environment**
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate   # For Windows
```

### **Step 3: Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**
Create a `.env` file in the project root and configure the required environment variables:
```plaintext
SECRET_KEY=your_secret_key
debug=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3  # or configure your database
```

### **Step 5: Run Migrations**
Apply database migrations:
```bash
python manage.py migrate
```

### **Step 6: Start the Server**
Start the Django development server:
```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

---

## **User Registration and Authentication**

### **Step 1: Register a User**
To register a new user, make a POST request to the `/api/accounts/register/` endpoint with the following JSON payload:
```json
{
    "username": "john_doe",
    "password": "securepassword",
    "email": "john@example.com",
    "bio": "Software Developer",
    "profile_picture": null
}
```

### **Step 2: Authenticate a User**
To authenticate a user and retrieve a token, make a POST request to the `/api/accounts/login/` endpoint with the following JSON payload:
```json
{
    "username": "john_doe",
    "password": "securepassword"
}
```

The response will include an authentication token:
```json
{
    "token": "your_auth_token"
}
```

### **Step 3: Use the Token for Authentication**
Include the token in the `Authorization` header for subsequent requests:
```http
Authorization: Token your_auth_token
```

---

## **Overview of the User Model**

The project uses a custom user model that extends Django’s `AbstractUser`. Below is a brief overview of the model:

### **Custom Fields:**
- **`bio`**: A text field to store user biographies.
- **`profile_picture`**: An image field to store profile pictures.
- **`followers`**: A `ManyToManyField` that allows users to follow other users.

### **Model Code:**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
```

---

## **API Endpoints**

### **User Endpoints:**
- **`POST /api/accounts/register/`**: Register a new user.
- **`POST /api/accounts/login/`**: Authenticate a user and retrieve a token.
- **`GET /api/accounts/profile/`**: Retrieve the authenticated user’s profile.

---

## **Troubleshooting**

1. **Migration Issues:**
   If you encounter migration errors, delete the migration files in the `migrations` folder (excluding `__init__.py`) and run:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Static Files:**
   If profile pictures are not loading, ensure you have configured media files properly in your `settings.py`:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```
   And update your `urls.py` to serve media files during development:
   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

---

## **Contributing**
Feel free to fork the repository and submit pull requests. Contributions are always welcome!

---

## **License**
This project is licensed under the MIT License.

POST /api/posts/
{
    "title": "My first post",
    "content": "This is the content of the post."
}

Response:
{
    "id": 1,
    "author": 1,
    "title": "My first post",
    "content": "This is the content of the post.",
    "created_at": "2024-12-20T10:00:00Z",
    "updated_at": "2024-12-20T10:00:00Z"
}



# API Documentation

## Like a Post
**Endpoint:** `/posts/<int:pk>/like/`
**Method:** `POST`
**Response:**
- Status 201: `{'status': 'post liked'}`
- Status 204: `{'status': 'post unliked'}`

## Fetch Notifications
**Endpoint:** `/notifications/`
**Method:** `GET`
**Response:** List of notifications for the current user.

# Simple Bank Application (Flask)

This is a minimal bank-style web application built using Python and Flask. It demonstrates:

- User login and session management
- Viewing balance and transaction history
- Transferring money between users

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000/`.

3. **Login** using the sample user:
   - **Username:** `employee`
   - **Password:** `password123`

4. Explore the dashboard and perform transfers.

## Project Structure

```
Dum/
├── app.py            # main Flask application
├── requirements.txt  # Python dependencies
├── README.md
├── templates/        # HTML templates
│   ├── layout.html
│   ├── login.html
│   ├── dashboard.html
│   └── transfer.html
├── static/           # static assets
│   └── css/style.css
└── public/           # existing public folder (redirects to Flask root)
    └── index.html
```

> **Note**: This is a simple proof-of-concept. For a production application, you should use a real database, secure password management, and proper error handling.
# securebank-internal-dashboard

# 💰 PennyWise Expense API

A professional-grade RESTful API built with **Django REST Framework** to help users track and manage personal finances. This project implements secure authentication, real-time spending aggregation, and interactive documentation, making it a robust foundation for any financial frontend.

---

## 🌟 Key Features

* **Secure JWT Authentication:** Industry-standard security using `djangorestframework-simplejwt`.
* **Dynamic Total Aggregation:** A custom pagination layer that calculates `total_spent` in real-time, automatically updating based on active search queries or category filters.
* **Advanced Filtering & Search:** Built-in support for filtering by **Category** or **Date**, and partial-match **Search** by title.
* **Interactive API Documentation:** Integrated **Swagger (OpenAPI 3.0)** UI for live exploration and testing of endpoints.
* **User Data Isolation:** Strict permission logic ensuring users can only interact with their own financial records.
* **Hyperlinked Navigation:** Fully discoverable API structure using hyperlinked relationships.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.12+, Django 5.0
* **API Framework:** Django REST Framework (DRF)
* **Security:** JSON Web Tokens (JWT) & Session Authentication
* **Database:** SQLite (Development)
* **Documentation:** `drf-spectacular` (Swagger/Redoc)

---

## 🚀 Quick Start

### 1. Setup Environment
```bash
git clone [https://github.com/yourusername/pennywise-api.git](https://github.com/yourusername/pennywise-api.git)
cd pennywise-api
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Database & Admin
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Explore the API
* **API Root:** `http://127.0.0.1:8000/api/expenses/`
* **Interactive Docs:** `http://127.0.0.1:8000/api/docs/`

---

## 📖 Key API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/token/` | POST | Obtain JWT Access & Refresh tokens |
| `/api/expenses/` | GET | List expenses (includes `total_spent` metadata) |
| `/api/expenses/` | POST | Create a new expense |
| `/api/categories/` | GET/POST | Manage expense categories |

---

## 🧪 Testing with Postman
1.  **POST** to `/api/token/` with your superuser credentials to receive the `access` token.
2.  In a new GET request to `/api/expenses/`, go to the **Authorization** tab.
3.  Select **Bearer Token** and paste your access token.
4.  The API will return your expenses and the dynamically calculated total for your current filtered view.

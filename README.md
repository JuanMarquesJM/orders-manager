<<<<<<< HEAD
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Orders Manager

A Django-based web application for managing orders, clients, and products.

## Key Features

- **Order Management:** Create, view, update, delete orders
- **Client Management:** Manage client information
- **Product Catalog:** Track product details
- **User Authentication:** Secure registration/login
- **Admin Interface:** Built-in Django admin panel

## Prerequisites & Dependencies

Ensure you have installed:
*   **Python:** 3.9 or higher
*   **pip:** Latest version
*   **Virtualenv** (recommended)
*   **Database:** SQLite (default), PostgreSQL or MySQL (for production)

Python dependencies (see `requirements.txt`):
* Django
* python-dotenv
* psycopg2-binary  # Only if using PostgreSQL

## Installation & Setup

1.  **Clone repository:**
    ```bash
    git clone https://github.com/JuanMarquesJM/orders-manager.git
    cd orders-manager
    ```

2.  **Create virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate    # Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment:**
    ```bash
    cp .env.example .env  # Create from template
    nano .env             # Edit with your values
    ```

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create admin user:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run development server:**
    ```bash
    python manage.py runserver
    ```
    Access at: http://localhost:8000

## Usage Guide

### Web Interface:
- Admin Panel: `/admin/`
- Orders Dashboard: `/orders/`
- Client Management: `/clients/`
- Product Catalog: `/products/`

## Configuration

Edit `order_manager/settings.py` for advanced settings:
```python
# Database (production example)
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Security settings for production
if not DEBUG:
    ALLOWED_HOSTS = ['.yourdomain.com']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
=======
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Orders Manager

A Django-based web application for managing orders, clients, and products.

## Key Features

- **Order Management:** Create, view, update, delete orders
- **Client Management:** Manage client information
- **Product Catalog:** Track product details
- **User Authentication:** Secure registration/login
- **Admin Interface:** Built-in Django admin panel

## Prerequisites & Dependencies

Ensure you have installed:
*   **Python:** 3.9 or higher
*   **pip:** Latest version
*   **Virtualenv** (recommended)
*   **Database:** SQLite (default), PostgreSQL or MySQL (for production)

Python dependencies (see `requirements.txt`):
* Django
* python-dotenv
* psycopg2-binary  # Only if using PostgreSQL

## Installation & Setup

1.  **Clone repository:**
    ```bash
    git clone https://github.com/JuanMarquesJM/orders-manager.git
    cd orders-manager
    ```

2.  **Create virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate    # Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment:**
    ```bash
    cp .env.example .env  # Create from template
    nano .env             # Edit with your values
    ```

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create admin user:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run development server:**
    ```bash
    python manage.py runserver
    ```
    Access at: http://localhost:8000

## Usage Guide

### Web Interface:
- Admin Panel: `/admin/`
- Orders Dashboard: `/orders/`
- Client Management: `/clients/`
- Product Catalog: `/products/`

## Configuration

Edit `order_manager/settings.py` for advanced settings:
```python
# Database (production example)
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Security settings for production
if not DEBUG:
    ALLOWED_HOSTS = ['.yourdomain.com']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
>>>>>>> 0c998079b8c8ce2aacb62fece2e8f1005cf598df

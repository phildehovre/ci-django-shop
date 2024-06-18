# Online Shop

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Setting Up Locally](#setting-up-locally)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Project Overview

### Context:
This project was created within the context of the Code Institute Full-Stack Bootcamp, February 2024 intake.

### Technical constraints:

The computer this project was developed on did not allow for the installation of node or npm. 
Developing using only vanilla JS is always an interesting constraint as it is easy to rely too much on contemporary front-end frameworks.

### The project:

This is an online shop built with Django, allowing users to browse products, add items to their cart, and complete purchases. It has a limited admin functionality that allows certain users to add and or edit products.

## Features

- User registration and authentication
- Product browsing and searching
- Shopping cart functionality
- Order and checkout process
- Potential payment integration
- Order history
- Admin panel for managing products, orders, and users

## Tech Stack

- **Backend:** Django, Django REST framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for development), PostgreSQL (for production)
- **Other:** Docker (for containerization), AWS S3 (for serving static files), Gunicorn (as WSGI HTTP Server)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Docker (optional, for containerization)

### Setting Up Locally

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/onlineshop.git
    cd onlineshop
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **(Optional) If using a JavaScript frontend:**

    ```bash
    cd frontend
    npm install
    npm start
    ```

## Usage

- Visit `http://127.0.0.1:8000/` to browse the shop.
- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage products, orders, and users.

## Configuration

- **Database Configuration:** Update the `DATABASES` setting in `settings.py` to configure your database.
- **Payment Integration:** Add your payment gateway API keys in the `settings.py`.
- **Email Settings:** Configure email backend and settings for sending order confirmations and other notifications.

## Testing

Run the tests using the following command:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact [your-email@example.com](mailto:your-email@example.com).


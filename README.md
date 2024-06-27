# Online Shop
## [Visit the shop](https://django-shop.up.railway.app/)

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

### Development:

I drew inspiration for the design from a widely recognized and highly popular online shopping platform. The objective of my implementation is to provide a comprehensive overview of the various facets involved in running an online shop. This high-level perspective aims to cover the essential components and functionalities without delving into the minutiae of each detail. Implementing every single aspect with full fidelity would be a significantly more time-consuming endeavor than the duration of this bootcamp permits.

#### Database implementation:

![Database diagram](https://github.com/phildehovre/ci-django-shop/assets/66724307/138cda10-9ae2-46a3-b874-4618990c60c3)

#### Project management:

By leveraging GitHub's robust tools for tracking progress and collaboration, our development team engaged in continuous interaction with users, gathering essential feedback at every stage. This feedback was instrumental in crafting detailed user stories, which were then meticulously divided into manageable tasks and organized into sprints. 

[Agile project view](https://github.com/users/phildehovre/projects/3/views/1)

![agile-screenshot](https://github.com/phildehovre/ci-django-shop/assets/66724307/85845972-3fea-4455-b690-af7ff621019a)

## Features

### User registration and authentication

![loginscreenshot](https://github.com/phildehovre/ci-django-shop/assets/66724307/789ca32a-2e94-4f16-9119-8cb0d39f9a34)

### Product browsing and searching
![amIresponsive](https://github.com/phildehovre/ci-django-shop/assets/66724307/ffa4d933-f67d-4cba-bf45-c21eafd65721)
  
### Shopping cart functionality
  ![basket](https://github.com/phildehovre/ci-django-shop/assets/66724307/43f2b3b2-012d-4af2-85dc-5de3d518e595)
  
### Order and checkout process
![checkout](https://github.com/phildehovre/ci-django-shop/assets/66724307/9e39e09e-06ee-4eff-ac34-693f12cea876)

### Mock payment integration
![mock_payment](https://github.com/phildehovre/ci-django-shop/assets/66724307/b25b279c-4de0-447e-9d03-492b19510959)

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
    git clone https://github.com/phildehovre/ci-django-shop.git
    cd ci-django-shop
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

## Usage

- Visit [the actual project](https://django-shop.up.railway.app/) to browse the shop.
- e-mail [me@philippedehovre.com](mailto:me@philippedehovre.com) to test the admin functionality

## Configuration

- **Database Configuration:** Update the `DATABASES` setting in `settings.py` to configure your database.

## Testing

No tests were implemented for this project.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request.

## License

Copyright 2024 Philippe De Hovre, all rights reserved.

## Contact

For any inquiries or issues, please contact [me@philippedehovre.com](mailto:me@philippedehovre.com).


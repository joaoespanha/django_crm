# Django CRM App

Welcome to the Django CRM app! This app is designed to help you manage your customer relationships efficiently.

## Getting Started

Follow these steps to set up and run the Django CRM app on your local machine.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python
- MySQL

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:joaoespanha/django_crm.git
   ```
2. Navigate to the app directory:

    ```bash
    cd crm_app
    ```
3. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Update the .env file with your MySQL credentials.

7. Initialize the MySQL database:

     ```bash
    python3 mydb.py
    ```

8. Set up Django's default tables::

     ```bash
    python3 manage.py migrate
    ```

9. Create a superuser for admin access:

     ```bash
    python3 manage.py createsuperuser
    ```

10. Start the development server:

     ```bash
    python3 manage.py runserver
    ```

11. Access the app in your browser at http://127.0.0.1:8000/.

## Usage

Use the Django CRM app to manage customer relationships, track interactions, and improve your business processes.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/fix: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.


## Created by: https://github.com/joaoespanha




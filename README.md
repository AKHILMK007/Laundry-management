# Laundry Management System

This is a Flask web application for managing laundry services. The application allows users to sign up, log in, and manage their laundry bags and history. It uses MySQL as the database for storing user and laundry data.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Database](#database)
- [Running the Application](#running-the-application)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Sign up and log in functionalities.
- **Manage Laundry Bags**: Users can manage their laundry bags, including adding, updating, and viewing details.
- **View Laundry History**: Users can view the history of their laundry activities.
- **Database**: MySQL database integration for data storage.

## Setup

1. Clone the repository:

    ```shell
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```shell
    cd <project_directory>
    ```

3. Install dependencies using pip:

    ```shell
    pip install -r requirements.txt
    ```

4. Configure the MySQL database:
    - Create a MySQL database named `laundry`.
    - Import the provided SQL dump (`washing-ton.sql`) into your database:

    ```shell
    mysql -u [username] -p [database_name] < washing-ton.sql
    ```

5. Set up your environment variables (if needed):
    - You may need to configure your database connection parameters in the application script (e.g., `app.py`).
    - Consider using environment variables for sensitive information like database credentials.

## Database

The application uses a MySQL database named `laundry`. The database contains the following tables:

- `bag`: Stores information about laundry bags.
- `bag_user`: Links users to their bags.
- `clothes`: Stores information about clothes in laundry bags.
- `employee`: Contains employee data (if needed).
- `laundry`: Contains laundry records and their status.
- `login_cred`: Stores user login credentials.
- `student`: Stores student data.

## Running the Application

To run the Flask application:

1. Navigate to the project directory.

2. Run the Flask application:

    ```shell
    flask run
    ```

    The application will start running on `http://127.0.0.1:5000/`.

## Routes

- `/`: Home page.
- `/login`: User login page.
- `/signup`: User signup page.
- `/home`: Home page after login.
- `/bag`: Bag management page.
- `/history`: Laundry history page.

## Contributing

Contributions to this project are welcome! If you find a bug or have a suggestion, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Laundry Management System! If you have any questions or issues, feel free to contact the repository maintainer.


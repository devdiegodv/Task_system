# Task System

![Task System](https://i.ibb.co/VHGmQbJ/task-system.png)

Task System is a Python Django-based CRUD (Create, Read, Update, Delete) system that allows users to manage tasks. It provides features for adding, deleting, editing, and updating tasks. Additionally, it offers user authentication through a login and registration system, allowing users to have their own accounts and view their own tasks.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Task Management**: Easily create, read, update, and delete tasks through a user-friendly web interface.

- **User Authentication**: Register for an account or log in to manage your own tasks securely.

- **User-Specific Task Lists**: Each user can only view and manage their own tasks, ensuring data privacy.

## Installation

To run Task System locally, follow these steps:

1. Clone the repository to your local machine using Git:

   ```shell
   git clone https://github.com/dev-diegov/Task_system.git
   ```
   
2. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

3. Activate the virtual environment:
    ```shell
   venv\Scripts\activate
   ```

4. Install the project dependencies:
    ```shell
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```shell
   python manage.py migrate
   ```

6. Create a superuser account to access the admin panel:
   ```shell
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```shell
   python manage.py runserver
   ```

The Task System should now be accessible locally at http://localhost:8000/.

## Usage

1. Access the application in your web browser.

2. Register for a new account or log in if you already have one.

![Login System](https://i.ibb.co/Zfsj2v0/login-system.png)
![Register System](https://i.ibb.co/zrQ98Zg/register-system.png)

3. Once logged in, you can:

- **Add a Task**: Click on the "+" button to create a new task.

- **Edit a Task**: Click on a task to edit its details.

- **Delete a Task**: Click on a task and then click the "X" button to remove it.

- **View Your Tasks**: Only your own tasks will be visible in the list.

4. To access the admin panel, visit http://localhost:8000/admin/ and log in with your superuser credentials.


## Contributing
Contributions are welcome! If you'd like to contribute to Task System, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix:
   ```shell
   git checkout -b feature/your-feature-name
   ```
   
4. Make your changes and commit them with descriptive commit messages.

5. Push your changes to your forked repository.

6. Create a pull request to the main branch of the original repository.

7. Wait for the maintainers to review and merge your pull request.

Please ensure that your code follows the project's coding standards and that you've added tests for your changes if applicable.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
```shell
You can copy and paste this Markdown content into your project's README.md file, and customize it further if needed.
```
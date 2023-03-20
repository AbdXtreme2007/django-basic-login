# django-basic-login
A Django project with simple login functionality

Setting up a Django Project:
Install Python: Make sure you have Python installed on your computer. You can download the latest version of Python from the official website.

Create a virtual environment: Open a command prompt or terminal window and navigate to the directory where you want to create your Django project. Then, run the following command to create a new virtual environment:

"python -m venv djangoenv"
This will create a new directory called djangoenv that contains a clean installation of Python and all the necessary tools for running a Django project.

Activate the virtual environment: To activate the virtual environment, run one of the following commands depending on your operating system:
On Windows:
djangoenv\Scripts\activate
On macOS or Linux:
source djangoenv/bin/activate
After running this command, your command prompt or terminal window should show that you are now working within the djangoenv virtual environment.

Install Django: With the virtual environment activated, run the following command to install Django:
pip install django
This will download and install Django and all its dependencies within your virtual environment.

Create a new Django project: To create a new Django project, run the following command:
django-admin startproject myproject
This will create a new directory called myproject that contains all the files and directories necessary for running a basic Django project.

Run database migrations: Before you can run your Django project for the first time, you need to apply any pending database migrations. To do this, navigate to your myproject directory (the one that contains manage.py) and run the following command:
python manage.py migrate
This will apply any pending database migrations and create any necessary tables in your database.

Run the development server: To start your Django project’s development server, run the following command from within your myproject directory:
python manage.py runserver
After running this command, open your web browser and navigate to http://127.0.0.1:8000/. You should see a “Welcome to Django” page indicating that your project is up and running

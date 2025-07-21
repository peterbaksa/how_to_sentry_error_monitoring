# How to Sentry Error Monitoring

This project is an example of how to connect and use the Sentry.io monitoring system.

## What is Sentry.io?

Sentry.io is a popular open-source error tracking and monitoring tool that helps developers identify, diagnose, and resolve issues in their applications. It captures errors and exceptions in real-time, providing detailed reports and context, which allows for faster debugging and improved application stability.

### Why do we need tools like Sentry.io?

In modern application development, especially with complex and distributed systems, it's crucial to have a robust monitoring solution. Tools like Sentry.io are essential for:
- **Proactive Issue Detection:** Catching errors before they impact a large number of users.
- **Faster Debugging:** Providing stack traces, request data, and environment context to quickly pinpoint the root cause of an error.
- **Improved User Experience:** By resolving issues quickly, you can ensure a smoother and more reliable experience for your users.
- **Performance Monitoring:** Identifying performance bottlenecks and understanding how your application behaves in production.

## Project Folder Structure

```
how_to_sentry_error_monitoring/
  - .env
  - _conda_create_env.bat
  - _conda_env_name.ini
  - _conda_install_requirements.bat
  - LICENSE
  - README.md
  - readme_images/
  - requirements.txt
  - src/
    - main.bat
    - main.py
```

## Setup

### 1. Create and Configure .env file

Before running the application, you need to create a `.env` file in the root directory of the project. This file will store your Sentry DSN.

```
SENTRY_PUBLIC_KEY = 
SENTRY_COMPANY_ID = 
SENTRY_PROJECT_ID =
```
You can get your DSN from your Sentry project settings.

![sentry find keys 1.png](readme_images%2Fsentry%20find%20keys%201.png)
![sentry find keys 2.png](readme_images%2Fsentry%20find%20keys%202.png)


### 2. Create Conda Environment

Run the following script to create a Conda environment with the specified Python version.
```bash
_conda_create_env.bat
```
The name of the conda environment is defined in `_conda_env_name.ini`.

### 3. Install Requirements

Run the following script to install all the necessary dependencies for this project.
```bash
_conda_install_requirements.bat
```

### 4. Run the Application

Now that the environment is prepared, you can run the FastAPI application.
Navigate to the `src` folder and run:
```bash
main.bat
```
The application will start on `http://localhost:8000`.

Successful execution will show a message in the terminal indicating that the application is running.

![succesfully_running_application.png](readme_images%2Fsuccesfully_running_application.png)



## Usage

Once the application is running, you can monitor its status on your Sentry.io dashboard.

### Triggering an Error

To see Sentry in action, you can intentionally trigger an error. Open your browser and go to the following URL:

[http://localhost:8000/error](http://localhost:8000/error)

This will execute a function that attempts to divide by zero, which will raise an exception. This error will be captured by Sentry, and you will be able to see the detailed error report in your Sentry project.



![zero_divide_error.png](readme_images%2Fzero_divide_error.png)

This is how it looks in sentry.io backend in Feed:
![error_in_sentry.io_feed.png](readme_images%2Ferror_in_sentry.io_feed.png)

You will also receive and email notification:
![error_sent_by_email.png](readme_images%2Ferror_sent_by_email.png)




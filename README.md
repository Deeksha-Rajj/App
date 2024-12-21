# App
Overview
This project is a web application designed to allow administrators to add Android apps and assign points for users who download them. Users can sign up, log in, view their profile, track completed tasks, and upload screenshots as proof of task completion. The application features an Admin Interface for managing apps and a User Interface for task tracking.

Key Features:
Admin Facing:

Admin can add Android apps and set points for tasks.
Manage user tasks and monitor their progress.
User Facing:

Users can sign up, log in, and view their profile.
Track tasks and upload screenshots as proof of completion.
Users earn points for completing tasks (e.g., downloading apps).
Task Completion:

Users are assigned tasks based on the apps added by the admin.
Each task is tracked, and points are awarded upon completion.
Screenshot upload feature for task verification.
API Endpoints:

RESTful APIs for managing apps and tasks.
Secure JWT authentication for user sign-in and profile management.
Installation
Follow these steps to get the project running on your local machine.

1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/app-points-system.git
cd app-points-system
2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
3. Install Dependencies
Install the necessary Python dependencies using pip.

bash
Copy code
pip install -r requirements.txt
4. Set up the Database
Run migrations to set up the database.

bash
Copy code
python manage.py migrate
Setup
1. Configure JWT Authentication
Make sure you have djangorestframework-simplejwt installed to handle JWT authentication.

Add the following to your settings.py:

python
Copy code
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'app_name',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
2. Static Files and Media
Configure Django to serve static and media files:

python
Copy code
# settings.py

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
Usage
Running the Application
To run the development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.

Endpoints
Here’s a list of key endpoints for both the Admin and User sides of the application.

Admin Endpoints:
POST /api/apps/
Create a new app (admin only). Requires app name, description, and points.

GET /api/apps/
List all apps (admin only).

GET /api/tasks/
View all tasks for users (admin only).

User Endpoints:
POST /signup/
Create a new user account (requires username, email, and password).

POST /login/
Login and obtain JWT token (requires username and password).

GET /user/profile/
View user profile (points earned, tasks completed).

POST /upload-screenshot/{task_id}/
Upload a screenshot to verify task completion.

Frontend
Drag-and-Drop Screenshot Upload
We use Dropzone.js for the screenshot upload interface, allowing users to drag and drop screenshots as proof of task completion.

Include this in your HTML template:

html
Copy code
<form action="/upload-screenshot/" class="dropzone" id="my-dropzone"></form>
<script src="https://cdn.jsdelivr.net/npm/dropzone@5.7.0/dist/dropzone.min.js"></script>
<script>
  Dropzone.autoDiscover = false;
  var myDropzone = new Dropzone("#my-dropzone", {
    url: "/upload-screenshot/",
    paramName: "screenshot",
    maxFiles: 1,
    maxFilesize: 5,  // Max size in MB
  });
</script>
#Security
Permissions and Authentication
Admin Endpoints: Only accessible by admin users. We use the IsAdminUser permission class for restricting access.
User Endpoints: Users must authenticate via JWT before accessing endpoints like profile and task management. The IsAuthenticated permission class ensures that only logged-in users can access these features.
#Contributing
We welcome contributions to enhance the features and security of the project.

#Steps to Contribute:
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add your feature').
Push to your branch (git push origin feature/your-feature).
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

#regex
Number Extraction from JSON Using Regex
Overview
This project demonstrates how to extract numbers from a given text using regular expressions (regex). The goal is to find all the numbers embedded in a JSON-like structure, which could represent an array of orders with IDs and error codes.

The numbers extracted could be useful for various tasks, such as analyzing user data, counting occurrences, or handling order IDs.

Features
Extracts all the numbers (IDs, error codes) from a JSON-like structure.
Uses regex for efficient pattern matching.
Python code that can be easily integrated into any project or script.
Installation
Ensure you have Python 3 installed on your machine. Then, follow these steps to get started:

1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/number-extraction.git
cd number-extraction
2. Install Dependencies
This project uses Python’s built-in re library, so no additional packages are required. If you're using any other dependencies, install them using:

bash
Copy code
pip install -r requirements.txt
Setup
1. Requirements
Python 3.x (use python3 to check your Python version).
A basic text editor or IDE to modify the code.
2. Running the Script
There is no special setup needed. You can directly run the script to extract numbers from the given JSON-like string.

Usage
1. Running the Script
Simply run the Python script, which contains the regex logic to extract numbers from the provided text:

bash
Copy code
python extract_numbers.py
2. Modifying the Input Text
You can modify the text variable in the script to include your own data in the same JSON-like format, and the script will extract all numbers accordingly.

Regex Pattern
The regex used to extract all numbers is:

regex
Copy code
\d+
\d stands for any digit (0-9).
+ means one or more of the preceding character (i.e., one or more digits).
This pattern will match all numbers in the text.
License
This project is licensed under the MIT License - see the LICENSE file for details.

PROBLEM 3 
A.
For scheduling periodic tasks, such as downloading a list of ISINs every 24 hours, I would recommend using cron jobs combined with a simple Python script or a task scheduler like APScheduler.
Why Cron Jobs or APScheduler?
Cron jobs are a classic and reliable solution for scheduling periodic tasks on Unix-based systems. They are simple to set up and have been around for decades, making them a time-tested method for task scheduling. By creating a cron job, we can easily set a task to run at a specific time or interval, such as downloading ISINs every 24 hours.
APScheduler is a great alternative when we want to handle task scheduling within a Python-based application. It allows us to schedule tasks in-memory, and provides flexibility to execute functions at specific intervals, which is ideal for periodic tasks like this. APScheduler is more suitable if you prefer having everything within your Python environment and don’t want to rely on external systems like cron.
Reliability and Scalability
Cron jobs are highly reliable, as they are managed by the operating system and are independent of any application logic. However, they lack flexibility in certain areas, such as dynamically adjusting the schedule or handling complex workflows.
APScheduler is also reliable and has built-in features to handle retries, job tracking, and error logging. It’s more flexible than cron jobs and integrates well with Python applications. However, scalability can be a challenge with APScheduler, especially if you need to schedule many tasks in parallel. As the number of tasks increases, maintaining performance and managing resources may become difficult.
Potential Problems in Production
Cron Jobs:
Limited Visibility: Cron jobs don’t provide built-in logging or error handling unless you explicitly set them up. It’s harder to monitor job failures and performance.
Hard to Scale: Cron jobs are limited to single machines and do not easily scale across multiple servers without additional configuration.
APScheduler:
Memory Usage: If tasks are long-running or require large memory allocations, APScheduler can lead to memory bloat or overload in your Python application.
Distributed Systems: APScheduler doesn’t natively support distributed task scheduling, so managing tasks across multiple servers could become complex without additional tools.
What Can Be Done for Scaling in Production?
For Cron Jobs:
You can use logging and alerting mechanisms to track task failures. Additionally, using a distributed cron system like Airflow can help scale cron jobs for more complex scenarios.
For scaling across multiple machines, tools like Rundeck or Airflow can be used to schedule and distribute cron jobs more effectively.
For APScheduler:
For better scalability, consider using Celery or RQ (Redis Queue), which provide distributed task queues, automatic retries, and worker management. These systems can handle periodic tasks in a much more scalable manner, especially when you need to process tasks across multiple servers.
Task Monitoring: Implement tools for monitoring the task scheduler, such as using a logging system or integrating with cloud-based services that can alert you to failures.
in conclusion :
For simple and small-scale periodic tasks, cron jobs or APScheduler are great options due to their simplicity and ease of use. However, for large-scale or mission-critical systems, it’s better to use more robust solutions like Celery or Airflow, which provide better scalability, error handling, and monitoring capabilities.


B.
Choosing between Flask and Django depends on the specific needs and complexity of the project, as well as the team's preferences and expertise.
choosing flask:
Microservice Architecture:
Flask is a lightweight, minimal framework that is perfect for building small, single-purpose applications or microservices. If you're building a microservice where the focus is on a specific task (e.g., an API endpoint or a small service), Flask’s simplicity and flexibility make it an ideal choice. It allows you to write minimal code and avoid unnecessary features.
Full Control Over Components:
Flask doesn’t come with many built-in tools (like an ORM, form handling, or admin panel). If you need more flexibility and want to hand-pick your libraries or design the structure of your app, Flask provides the freedom to choose how to implement each part. For example, you can integrate any database or use the tools that best fit your needs.
Small to Medium-Sized Applications:
If you’re working on a project that is relatively small and doesn't require complex features out-of-the-box, Flask’s minimalistic nature makes it an easy and quick choice. It allows for rapid development and deployment with minimal overhead.
Learning and Experimentation:
Flask’s simplicity makes it a great choice for learning the fundamentals of web development. If you're building a small project to explore a new concept or experiment with new technologies (e.g., machine learning model APIs), Flask provides the necessary simplicity without too many constraints.
Faster Prototyping:
Flask’s minimalism allows you to quickly create prototypes and MVPs (Minimum Viable Products). If you’re under tight deadlines or need to iterate on ideas quickly, Flask is great for getting something up and running fast.

choosing django:
Feature-Rich Applications:
Django comes with many built-in features like an admin panel, authentication, ORM, form handling, and security tools. If you’re building a more feature-rich web application (e.g., an e-commerce site, social media platform, or content management system), Django’s batteries-included philosophy saves time by providing most of what you need out of the box.
Scalability and Complex Applications:
If you’re working on a large-scale application where future scalability is a concern, Django is a better fit. Its built-in tools, like the ORM, admin interface, and user management system, are designed to scale well. Django’s structure encourages best practices like the Model-View-Template (MVT) pattern, which can help in maintaining and scaling the application as it grows.
Standardization and Convention Over Configuration:
Django follows a more opinionated approach to application structure, which means it enforces certain patterns and conventions. If your project requires a standardized development process, Django provides this out-of-the-box. This is useful in teams where you want to ensure consistency across codebases and make onboarding new developers smoother.
Security:
Django has many built-in features to enhance security, such as protection against SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF). If security is a major concern in your project (e.g., handling sensitive user data, financial transactions), Django’s robust security features can help you avoid common pitfalls.
Rapid Development of Larger Applications:
If you're building an application with more complex user interactions, admin functionality, or a large amount of data processing, Django’s integrated tools (like its powerful ORM and built-in authentication) speed up the development process significantly. Django’s structure and rich ecosystem are built to handle large projects efficiently, especially if you need to include a variety of different app components.
Team Collaboration:
Django’s standardized approach makes it easier for multiple developers to collaborate on a project. Its well-defined project structure helps developers quickly understand the flow and architecture, which is beneficial for larger teams.

in conclution
Flask is ideal for smaller projects, APIs, microservices, and prototypes, where flexibility and simplicity are the key. It’s the go-to option when you want to start small and have full control over the tools and components you use.
Django, on the other hand, shines in larger, feature-complete applications, where rapid development, security, scalability, and built-in tools are important. It's perfect for enterprise-level applications or any project requiring a robust framework with a lot of built-in functionality.







 emplService
# API Documentation
Authentication
POST /api/token/: Get JWT token by providing valid username and password in the request body.
POST /api/token/refresh/: Refresh JWT token by providing valid refresh token in the request body.
Creating Restaurant
POST /api/restaurants/: Create a new restaurant by providing valid name and address in the request body.
Uploading Menu for Restaurant
POST /api/restaurants/<restaurant_id>/menus/: Upload menu for a restaurant with the given restaurant_id and date in the request body. Each menu is unique to a date, so providing a new menu for the same date will override the previous menu.
Creating Employee
POST /api/employees/: Create a new employee by providing valid username, password, and restaurant_id (optional) in the request body. If restaurant_id is provided, the employee will be associated with that restaurant. If not, the employee will be created without any association.
Getting Current Day Menu
GET /api/menus/: Get the menu for the current day.
Getting Results for the Current Day
GET /api/results/: Get the results for the current day.
Running the System
To run the system, follow these steps:

Clone the repository.
Install Docker and docker-compose.
Build the Docker image by running docker-compose build.
Start the system by running docker-compose up.
The API will be accessible at http://localhost:8000.
Running the Tests
To run the tests, follow these steps:

Make sure the system is not currently running.
Build the Docker image by running docker-compose build.
Run the tests by running docker-compose run app sh -c "python manage.py test && flake8".

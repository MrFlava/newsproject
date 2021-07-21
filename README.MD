Steps to run on localhost:

    1. Clone the project using git clone
    2. Install all requirement modules using pip 
    3. In the main directory  (newsproject) create local_settings.py with SECRET_KEY and database settings
    4. Update database with migrations ( just type python manage.py migrate )
    5. Run the app using python manage.py runserver

Steps to run with docker-compose:

    1. Clone the project using git clone
    2. Type this command: sudo docker-compose up --force-recreate
    3. In the main directory  (newsproject) create local_settings.py with SECRET_KEY and database settings
    4. Run the docker-compose server : sudo docker-compose run web python manage.py runserver 0.0.0.0:8000


After that, you can use Postman for testing this API. All necessary endpoints stored in the Postman collection.

    



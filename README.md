# Django Firebase App

Backend service REST API for shopping and ordering application based on Django and Firebase.

## Project Structure

- `django_firebase`: main service of application
- `api_auth`: app for authentication

## Project Setup

### Installation
1. Install pipenv
`pip3 install pipenv`
2. Clone the repository.
3. `cd` into `django_firebase` directory and run `pipenv install -r requirements.txt` to install necessary dependencies.
4. Create a virtualenv in the root of project with `pipenv shell` and activate the virtualenv.
5. Create a `.env` file in the same directory as `settings` to store environment variables.

### Database Migration
Make sure you are in the same directory as `manage.py`, then run the following to develop:
1. Run `python manage.py makemigrations` to stage migrations
2. Then run `python manage.py migrate` to write the migrations to the database schema.
3. To boot the development server and use the API, run `python manage.py runserver`. 

### Creating an Admin User

Follow these steps to create a Django admin (superuser) user account, for the Django admin interface:
1. Activate your virtualenv.
2. `cd` into the `Neer-Algorithm` directory, where `manage.py` is located.
3. Run `python manage.py createsuperuser`, and enter appropriate values into the prompts.
4. To access the admin web interface, run `python manage.py runserver` to boot the dev server, and then navigate to `localhost:8000/admin` in your web browser.

### API Endpoints

You can use [postman](https://www.postman.com) to test the api during development.

#### Authentication

- Create new user: `/api/auth/signup`. Verbs: `POST`

You can try `http://127.0.0.1:8000/api/auth/signup` and send json data as example following to test:

```
{
    "username": "testuser",
    "first_name": "Test",
    "last_name": "User",
    "email": "testuser@gmail.com",
    "password1": "password",
    "password2": "password"
}
```

After validations the service will created user in Firebase Authentication and push data info into Firebase database. The correct response should be like:
```
{
    "username": "testuser",
    "email": "testuser@gmail.com",
    "first_name": "Test",
    "last_name": "User"
}
```

- Login existing user: `/api/auth/login`. Verbs: `POST`

You can try `http://127.0.0.1:8000/api/auth/login` and send json data as example following to test:

```
{
    "email": "testuser@gmail.com",
    "password": "password"
}
```

If authenticated, the response should be like:

```
{
    "first_name": "Test",
    "localId": <localId>,
    "idToken": <idToken>,
    "refreshToken": <refreshToken>
}
```

### Reference
1. [Django Restframework](https://www.django-rest-framework.org)
2. [Django Documentation](https://docs.djangoproject.com/en/3.0/)
3. [Pyrebase](https://github.com/thisbejim/Pyrebase)
4. [Installation & Setup for Firebase REST API](https://firebase.google.com/docs/database/rest/start)


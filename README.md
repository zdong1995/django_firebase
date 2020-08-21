# Django Firebase App

Backend service REST API for shopping and ordering application based on Django and Firebase.

## Project Structure

- `django_firebase`: main service of application
- `api_auth`: app for authentication
- `payment`: app for payment service

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

### API Endpoints


You can use [postman](https://www.postman.com) to test the api during development using the API test collection created by Andy Dong:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/7deeb5f8342727365897)


#### Auth

- Create new user: `/api/auth/register`. Verbs: `POST`
- Login: `/api/auth/login`. Verbs: `POST`
- Email Verify: `/api/auth/email_verify`. Verbs: `POST`
- Reset Password: `/api/auth/reset_password`. Verbs: `POST`
- Update Auth: `/api/auth/update`. Verbs: `POST`
- Add Info: `/api/auth/add_info`. Verbs: `POST`

#### Payment - Customer
- Create a customer: `/api/stripe/customer/add`. Verbs: `POST`
- Get customer info: `/api/stripe/customer`. Verbs: `GET`
- Update customer info: `/api/stripe/customer`. Verbs: `POST`
- Delete customer: `/api/stripe/customer`. Verbs: `DELETE`

#### Payment - Card
- Add a card: `/api/stripe/card/add`. Verbs: `POST`
- Get a card info: `/api/stripe/card`. Verbs: `GET`
- Update card info: `/api/stripe/card`. Verbs: `POST`
- Delete a card: `/api/stripe/card`. Verbs: `DELETE`
- Get all cards of one customer: `/api/stripe/card/list`. Verbs: `GET`
- Set default card of one customer: `/api/stripe/default`. Verbs: `POST`

#### Payment - Charge
- Create a charge: `/api/stripe/charge/add`. Verbs: `POST`
- Get a charge info: `/api/stripe/charge`. Verbs: `GET`
- Recent transactions: `/api/stripe/transaction`. Verbs: `GET`
- Add a refund: `/api/stripe/refund/add`. Verbs: `POST`
- Get a refund info: `/api/stripe/refund`. Verbs: `GET`

### Reference
1. [Django Restframework](https://www.django-rest-framework.org)
2. [Django Documentation](https://docs.djangoproject.com/en/3.0/)
3. [Pyrebase](https://github.com/thisbejim/Pyrebase)
4. [Installation & Setup for Firebase REST API](https://firebase.google.com/docs/database/rest/start)
5. [Stripe API Doc](https://stripe.com/docs/api)

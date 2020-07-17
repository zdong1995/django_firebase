import pyrebase

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api_auth.serializers import SignupSerializer, LoginSerializer

config = {
    'apiKey': "AIzaSyDaqtcp2Z3g5llZNbzOix63ICH7CJ1u6DM",
    'authDomain': "django-firebase-app.firebaseapp.com",
    'databaseURL': "https://django-firebase-app.firebaseio.com",
    'projectId': "django-firebase-app",
    'storageBucket': "django-firebase-app.appspot.com",
    'messagingSenderId': "475600225433",
    'appId': "1:475600225433:web:5c3d1d614f2d08ec262408"
}

firebase = pyrebase.initialize_app(config)
f_auth = firebase.auth()
f_database = firebase.database()


class SignupView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        if data['password1'] != data['password2']:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Password must match."})

        # build new data frame for auth and database push
        password = data['password1']
        data['password'] = password
        del data['password1']
        del data['password2']

        try:
            # create authentication info in firebase authentication
            user = f_auth.create_user_with_email_and_password(email, password)
            print(user)
            uid = user['localId']  # primary key of user
            # push to database -> user/uid/details/data
            f_database.child("users").child(uid).child("details").set(data)
        except:
            message = "User information has already existed. Please try again."
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        try:
            f_auth.send_email_verification(user['idToken'])
        except:
            return Response({'detail': 'Invalid email address.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SignupSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'msg': 'Email and password can not be empty.'})

        try:
            # authentication and retrieve response message
            user = f_auth.sign_in_with_email_and_password(email, password)
            # search database to find corresponding attribute "first_name"
            uid = user["localId"]
            name = f_database.child("users").child(uid).child("details").child("first_name").get()
            user['first_name'] = name.val()
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED,
                            data={'msg': 'Invalid credentials. Please try again.'})

        serializer = LoginSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ResetPaswordView(GenericAPIView):

    pass

class EmailVerifyView(GenericAPIView):

    def post(self, request):
        idToken = request.data.get('idToken')

        try:
            f_auth.send_email_verification(idToken)
        except:
            return Response({'detail': 'Invalid email address.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Email sent successful to your email. Please verify your email address.'},
                        status=status.HTTP_200_OK)


class UpdateView(GenericAPIView):

    pass

class AddView(GenericAPIView):

    pass
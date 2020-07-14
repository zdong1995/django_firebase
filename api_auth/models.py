from django.db import models


class AuthenticatedUser(models.Model):
    first_name = models.CharField(max_length=10, null=False)
    localId = models.CharField(max_length=250)
    idToken = models.CharField(max_length=1000)
    refreshToken = models.CharField(max_length=250)


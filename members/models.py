from django.db import models

'''
Class Members - becomes a database table
Attributes firstname, lastname - become table fields
'''


class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    town = models.CharField(max_length=50)

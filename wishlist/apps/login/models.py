from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import date

class UserManager(models.Manager):
    def add_user(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "Name must be present and more than 3 characters"

        if len(postData['username']) < 3:
            errors['username'] = "Username must be present and more than 3 characters"

        if self.filter(username = postData['username']):
            errors['username'] = "Username already exists"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password does not match"

        if not postData['hire_date'] <= str(date.today()):
            errors['hire_date'] = "You are not from the future"

        if not postData['hire_date']:
            errors['hire_date'] = "Must enter a date"


        else:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(name = postData['name'], username = postData['username'], hire_date = postData['hire_date'], password = hashed_password)

        return errors

    def hash_new_pw(self, password_in):
        return bcrypt.hashpw(password_in.encode(), bcrypt.gensalt())

    def check_pw_db(self, password_in, hashed_db_password):
        return bcrypt.checkpw(password_in.encode(), hashed_db_password.encode())

    def check_user(self, postData):
        errors = {}

        if not postData['username']:
            errors['username'] = "Must enter user name"

        if not postData['password']:
            errors['password'] = "Must have a password"

        if errors:
            return errors

        else:
            try:
                tryMe = User.objects.filter(username = postData['username'])

            except:

                errors['nope'] = "Sorry, invaild login information"
            return errors

        if User.objects.check_pw_db(postData['password'], tryMe.password):
            return tryMe.id

        else:

            errors['nope'] = "sorry, invaild login information"
        return errors





class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

# Create your models here.

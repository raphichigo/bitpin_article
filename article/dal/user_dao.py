# todo: we should have user or identity app for user works and its just for now that user_dao is in article app
from django.contrib.auth.models import User


class UserDao:
    def __init__(self):
        ...

    def get_user_by_id(self, user_id):
        return User.objects.filter(id=user_id).first()

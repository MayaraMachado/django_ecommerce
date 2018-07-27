from django.contrib.auth.backends import ModelBackend as BaseModelBackends
from accounts.models import User

class ModelBackend(BaseModelBackends):
    
    def authenticate(self, username=None, password=None):
        if not username is None:
            try:
                user = User.objects.get(email=username)
                if(user.check_password(password)):
                    return user
            except User.DoesNotExist:
                pass
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# Emailで認証する方法を選択肢を増やす

class EmailAuthBackend(BaseBackend):

    def authenticate(self, request, email, password):
        print("EmailAuthBackendが呼び出されている")
        print(request, email, password)
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    print("認証成功！！！")
                    return user
        return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

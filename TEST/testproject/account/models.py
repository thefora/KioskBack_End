from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class k_userManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        try:
            if not phone:
                raise ValueError('User must have a phone-number')
            user = self.model(
                phone = phone,
            )

            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)

            user.set_password(password)
            user.is_active = True
            user.save()

            return user

        except Exception as e:
            print(e)

    def create_superuser(self, username, password=None, **extra_fields):
        try:
            superuser = self.create_user(
                username = username,
            )
            superuser.is_admin = True
            superuser.is_superuser = True
            superuser.is_active = True
            superuser.is_staff = True
            superuser.save()
            return superuser
        except Exception as e:
            print(e)


class k_user(AbstractBaseUser):
    phone = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=6)
    branch = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    birth = models.DateField(max_length=16)
    sex = models.CharField(max_length=2)
    

    objects = k_userManager()

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone'

class k_user_information(models.Model):
    
    user_phone = models.ForeignKey("k_user", related_name="user", on_delete=models.CASCADE, db_column="user_phone")
    qrcode = models.CharField(max_length=25)
    branch_now = models.CharField(max_length=30)
    service_time = models.IntegerField(5)
    rest_time = models.IntegerField(5)
    exit_time = models.DateField(max_length=16)
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    # 자동으로 해당 시간이 추가되게 해놓음
    email = models.EmailField(verbose_name="email", max_length=60, default = "마이페이지에서 이름을 입력해주세요!")
    interest = models.CharField(verbose_name='interest', max_length=200)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last joined", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(max_length=255, upload_to="img/", null=True, blank=True, default="img/Bin.png")

    # User 객체가 생성되었을 때 자동으로 연결된 Profile 객체가 생성되게 한다.
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def __str__(self):
        return str(self.user)

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username.")
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# def get_profile_image_filepath(self, filename):
#     return f'profile_images/{self.pk}/{"profile_image.png"}'

# def get_default_profile_image():
#     return "img/Bin.png"

# class Profile(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="last joined", auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)

#     objects = MyAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username
    
#     def get_profile_image_filename(self):
#         return str(self.progile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
    
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
    
#     def has_module_perms(self, app_label):
#         return True

# class MyUserAuth(BaseBackend):
#     def authenticate(self, request, email = None, password = None, **kwargs):
#         print("DEBUG")
#         try:
#             user = get_user_model().objects.get(email = email)
#         except:
#             return None
#         if str(user.password) == hashlib.sha256(password).hexdigest():
#             return user
#         else:
#             return None
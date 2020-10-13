from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self,email,fullname,username,phone_number,password=None):
        if not email:
            raise ValueError('email required')
        if not fullname:
            raise ValueError('full name required')
        if not username:
            raise ValueError('user name required')
        if not phone_number:
            raise ValueError('phone number required')

        #all fields are ok
        user = self.model(
            email = self.normalize_email(email),
            fullname = fullname,
            username =username,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,email,fullname,username,phone_number,password):
        user = self.create_user(
            email= self.normalize_email(email),
            fullname = fullname,
            username = username,
            phone_number = phone_number,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user
   


class useraccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=30,unique=True)
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13) 
    #password = models.CharField(max_length=50)
    #image = models.ImageField(blank = True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname','username','phone_number']
    
    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj = None):
        return self.is_admin
    def has_module_perms(self,applabel):
        return True

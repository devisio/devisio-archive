from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):
    def create_account(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = BaseUserManager.normalize_email(email)

        account = self.model(email=email, last_login=now, **extra_fields)
        account.set_password(password)
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    username = models.CharField(_("Username"), max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(_("Email address"), unique=True, db_index=True, blank=False, null=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

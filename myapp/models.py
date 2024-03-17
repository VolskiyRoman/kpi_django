from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='myapp_user_groups',
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='myapp_user_permissions',
        related_query_name="user",
        help_text=_('Specific permissions for this user.'),
    )


class Order(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(User, related_name='orders_as_customer', on_delete=models.CASCADE)
    performer = models.ForeignKey(User, related_name='orders_as_performer', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()

    user = models.ForeignKey(User, related_name='reviews_as_user', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='reviews_as_reviewer', on_delete=models.CASCADE)

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Рейтинг повинен бути числом від 1 до 5.")

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)


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
        if self.rating not in range(1, 6):
            raise ValidationError('Rating must be from 1 to 5')

    def save(self, *args, **kwargs):
        self.full_clean()  # Проводимо повну валідацію перед збереженням
        super().save(*args, **kwargs)

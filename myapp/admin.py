from django.contrib import admin
from .models import Order, Review  # Імпорт моделей з вашого додатку


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'performer', 'completed')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'rating', 'user', 'reviewer')


from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('user_page/<int:user_id>/', views.user_page, name='user_page'),
    path('user_page/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/mark_as_completed/', views.mark_order_as_completed, name='mark_as_completed'),
    path('create_review/<int:user_id>/', views.create_review, name='create_review'),
    path('reviews/', views.review_list, name='review_list'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
]

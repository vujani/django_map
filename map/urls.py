from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('contacts/', views.contacts, name='contacts'),
    path('faq/', views.faq, name='faq'),
    path('info/', views.info, name='info'),
    path('terms_of_use/', views.ternms_of_use, name='terms_of_use'),
    path('my_tags/', views.my_tags, name='my_tags'),
    path('admin_tags/', views.admin_tags, name='admin_tags'),
]
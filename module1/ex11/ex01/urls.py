from django.urls import path
from . import views

urlpatterns = [
    path('django', views.djangopage),
    path('display', views.displaypage),
    path('templates', views.templatespage),
]

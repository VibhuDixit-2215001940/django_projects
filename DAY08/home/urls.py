from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('success',views.success,name="success"),
    path("invalid",views.invalid,name="invalid")
]
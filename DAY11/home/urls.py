from . import views
from django.urls import path
urlpatterns = [
    path('',views.login),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('Signup/',views.Signup,name="Signup"),
    path('Invalid/',views.Invalid,name="Invalid"),
    path('logout/',views.logout)
]

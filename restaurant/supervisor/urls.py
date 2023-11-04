from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("/login", views.login1),
    path("/logout", views.logout_view),
    path("/required", views.required),
    path("/delete_instants", views.delete_instants),
    path("/checkout", views.checkout),
]

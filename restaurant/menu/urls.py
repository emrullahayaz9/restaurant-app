from django.urls import path
from . import views
urlpatterns = [
    path("/page", views.login_page),
    path("/page/<int:id>", views.menu),
]

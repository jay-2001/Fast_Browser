from django.urls import path

from . import views

# app_name = "email"


urlpatterns = [
    path("gmail/", views.index, name="index"),
    path("gmail/login/", views.login_view, name="login"),
    path("gmail/logout/", views.logout_view, name="logout"),
    path("gmail/register/", views.register, name="register"),

    # API Routes
    path("emails", views.compose, name="compose"),
    path("emails/<int:email_id>", views.email, name="email"),
    path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
    path("emails/search/<str:query>", views.search, name="search"),
]

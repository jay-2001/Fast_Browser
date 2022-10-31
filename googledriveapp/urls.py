from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = "drive"

urlpatterns = [
    path("drive/", views.drive_index, name="drive_index"),
    path("drive/drive_login/", views.drive_Login, name="drive_login"),
    path("drive/drive_signup/",views.drive_SignUp,name="drive_signup"),
    path("drive/drive_folder/<int:folderid>/",views.drive_folder, name="drive_folder"),
    path("drive/drive_addFolder/", views.drive_addfolder, name="drive_addfolder"),
    path("drive/drive_logout/", views.drive_Logout, name="drive_logout"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

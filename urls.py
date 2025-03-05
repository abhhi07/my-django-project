from django.contrib import admin
from django.urls import path
from main import views  # Import views from main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page URL
]

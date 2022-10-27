from django.urls import path
from .views import get_profile

# adjacent

urlpatterns = [
    path("", get_profile, name="profile-get")
]
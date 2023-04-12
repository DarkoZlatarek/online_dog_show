from . import views
from django.urls import path


urlpatterns = [
    path('', views.EntriesList.as_view(), name='home')
]

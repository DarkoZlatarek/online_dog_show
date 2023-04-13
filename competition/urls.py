from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('competition/', views.EntriesList.as_view(), name='competition')
]

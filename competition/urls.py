from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('enter/', views.enter_submit, name='enter'),
    path('edit/<slug:slug>', views.edit_entry, name='edit_entry'),
    path('delete/<slug:slug>', views.delete_entry, name='delete_entry'),
    path('competition/', views.EntriesList.as_view(), name='competition'),
    path('<slug:slug>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('like/<slug:slug>', views.EntryLike.as_view(), name='entry_like')
]

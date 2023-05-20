from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home'),
    path('rules/', views.rules_page, name='rules'),
    path('enter/', views.enter_submit, name='enter'),
    path('edit/<slug:slug>', views.edit_entry, name='edit_entry'),
    path('delete/<slug:slug>', views.delete_entry, name='delete_entry'),
    path('all_entries/', views.EntriesList.as_view(), name='all_entries'),
    path('competition/', views.CurrentOrderList.as_view(), name='competition'),
    path('<slug:slug>/', views.EntryDetail.as_view(), name='entry_detail'),
    path('like/<slug:slug>', views.EntryLike.as_view(), name='entry_like')
]

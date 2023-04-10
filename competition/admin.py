from django.contrib import admin
from .models import Enter
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Enter)
class EnterAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')

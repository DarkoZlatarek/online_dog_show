from django.contrib import admin
from .models import Enter
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Enter)
class EnterAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


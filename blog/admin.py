from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class postadmin(SummernoteModelAdmin):
    date_hierarchy = "publish_date"
    list_display=('titel','cuntent_view','status','publish_date',)
    list_filter=('status','publish_date')
    summernote_fields = ('content')

class commentadmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display=('subject','post','aproved','created_date',)


admin.site.register(comment,commentadmin)
admin.site.register(categore)
admin.site.register(post,postadmin)
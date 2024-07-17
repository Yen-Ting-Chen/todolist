from django.contrib import admin
from show_list import models

# Register your models here.
class do_list_Admin(admin.ModelAdmin):
    list_display = ('title','description','deadline','pub_time')

admin.site.register(models.do_list,do_list_Admin)

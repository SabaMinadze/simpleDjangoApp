# simpleApp/admin.py
from django.contrib import admin
from .models import BigBox

class BigBoxAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age")


admin.site.register(BigBox, BigBoxAdmin)


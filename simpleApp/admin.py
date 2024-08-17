from django.contrib import admin
from .models import BigBox, Offer


class BigBoxAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")    

admin.site.register(BigBox, BigBoxAdmin)
admin.site.register(Offer, OfferAdmin)
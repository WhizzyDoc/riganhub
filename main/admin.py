from django.contrib import admin
from .models import *

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'ceo', 'email', 'tel', 'address']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'image']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject']

admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Developer)
admin.site.register(Expertize)
admin.site.register(Faq)
admin.site.register(Gallery)
admin.site.register(Feature)

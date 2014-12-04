from django.contrib import admin
from foundation.models import Page, Headermenu, Title, Portfolio, Develop, Information

class PageAdmin(admin.ModelAdmin):
    list_display =('title',)
    prepopulated_fields = {'slug':('title',)}
    
class HeadermenuAdmin(admin.ModelAdmin):
    list_display =('name', 'url')
    prepopulated_fields = {'url':('name',)}


    
admin.site.register(Page,PageAdmin)
admin.site.register(Headermenu, HeadermenuAdmin)
admin.site.register(Title)
admin.site.register(Portfolio)
admin.site.register(Develop)
admin.site.register(Information)

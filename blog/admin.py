from django.contrib import admin
from .models import contactus, userProfile, blog


class contactusAdmin(admin.ModelAdmin):
    list_display =('fullname', 'phone_num', 'email', 'message')

admin.site.register(contactus, contactusAdmin)


class userProfileAdmin(admin.ModelAdmin):
    list_display =('phone_num', 'age')

admin.site.register(userProfile, userProfileAdmin)


class blogAdmin(admin.ModelAdmin):
    list_display =('category', 'title', 'date_created', 'image', 'description' )

admin.site.register(blog, blogAdmin)
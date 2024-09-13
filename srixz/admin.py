from django.contrib import admin
from .models import SiteSetting
from .models import *
from django.utils.html import format_html


class Imageinline(admin.TabularInline):
    model=Galleryimage
    extra=1



class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value',)
    list_filter = ('key',)
    search_fields = ('key', 'value')
    fields = ('key', 'value', 'image')

    
    

 
    
admin.site.register(SiteSetting,SiteSettingAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','imageview',)
    list_filter = ('title',)

    

admin.site.register(Category,CategoryAdmin)


class GalleryAdmin(admin.ModelAdmin):
    inlines=[Imageinline]
    list_display=('title','category','date',)
    list_filter = ('title','category','date',)

admin.site.register(Gallery,GalleryAdmin)


class GalleryimageAdmin(admin.ModelAdmin):
    list_display=('gallery','imageview',)
    list_filter = ('gallery',)

    


    def has_add_permission(self, request): # Here
        return not Galleryimage.objects.exists()

admin.site.register(Galleryimage,GalleryimageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','mobile_1','mobile_2','address','place','city','district','pincode','email')
    
    def has_add_permission(self, request): # Here
        return not Contact.objects.exists()
    
admin.site.register(Contact,ContactAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display=('name','about_me','my_mission','imageview')


    
    
    def has_add_permission(self, request):
    # Return False to disable the option to add new records
        return False
    
admin.site.register(About,AboutAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','description','imageview')
    list_filter = ('title',)
    


admin.site.register(Service,ServiceAdmin)


class EnquiryAdmin(admin.ModelAdmin):

    list_display=('firstname','lastname','email_link','subject','message')
    readonly_fields = ('firstname', 'lastname', 'email', 'subject', 'message')
    list_filter = ('firstname','email',)
   
    
    def email_link(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'

    def has_add_permission(self, request):
    # Return False to disable the option to add new records
        return False


    
admin.site.register(Enquiry,EnquiryAdmin)

class Banneradmin(admin.ModelAdmin):
    list_display=('text','imageview')

    

admin.site.register(Banner,Banneradmin)
# myapp/models.py
from django.db import models
from django.utils.html import mark_safe

class SiteSetting(models.Model):
    SITE_NAME = 'site_name'
    LOGO_IMAGE = 'logo_image'
    INSTAGRAM_LINK = 'instagram_link'
    PINTREST_LINK = 'pintrest_link'
    FACEBOOK_LINK = 'facebook_link'
    YOUTUBE_LINK = 'youtube_link'
    
    KEY_CHOICES = [
        (SITE_NAME, 'Site Name'),
        (LOGO_IMAGE, 'Logo Image'),
        (INSTAGRAM_LINK, 'Instagram Link'),
        (PINTREST_LINK, 'Pintrest link'),
        (FACEBOOK_LINK, 'Facebook link'),
        (YOUTUBE_LINK, 'Youtube link'),
    ]
    
    key = models.CharField(max_length=255, choices=KEY_CHOICES, unique=True)
    value = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.key

    @property
    def is_logo(self):
        return self.key == self.LOGO_IMAGE
    
    def imageview(self):
        return mark_safe(
                        '<a href="%s" >'
                        '<img src="%s" width="80" height="80" />'
                        '</a>' % (self.image.url, self.image.url)
                    )
        return "No Image" 

    
    
    
class Category(models.Model):
    title=models.CharField(max_length=200)
    cover_image=models.ImageField(upload_to="category_cover/")
    
    def __str__(self) :
        return self.title
    
    def imageview(self):
        return mark_safe(
                        '<a href="%s" >'
                        '<img src="%s" width="80" height="80" />'
                        '</a>' % (self.cover_image.url, self.cover_image.url)
                    )
        return "No Image" 
    
    
    
class Gallery(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(auto_now=True)
    description=models.CharField(max_length=300,null=True,blank=True)


    def __str__(self):
        return self.title
    
    
    
    
    



class Galleryimage(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    show_in_gallery=models.BooleanField(default=True)



    def __str__(self):
        return self.gallery.title


    def imageview(self):
        return mark_safe(
                        '<a href="%s" >'
                        '<img src="%s" width="80" height="80" />'
                        '</a>' % (self.image.url, self.image.url)
                    )
        return "No Image"    
    
    
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile_1=models.CharField(max_length=10)
    mobile_2=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    email=models.EmailField()
    
    
    def __str__(self):
        return self.first_name
    
    
class About(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='about_cover/')
    about_me=models.TextField()
    my_mission=models.TextField()
    
    def imageview(self):
            return mark_safe(
                            '<a href="%s" >'
                            '<img src="%s" width="80" height="80" />'
                            '</a>' % (self.image.url, self.image.url)
                        )
            return "No Image"     
    
    
class Service(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    price=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to='service_cover/')
    
    def __str__(self) :
        return self.title

    def imageview(self):
        return mark_safe(
                        '<a href="%s" >'
                        '<img src="%s" width="80" height="80" />'
                        '</a>' % (self.image.url, self.image.url)
                    )
        return "No Image" 


class Enquiry(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return self.email


class Banner(models.Model):
    text=models.CharField(max_length=300)
    image=models.ImageField(upload_to='bannerimage/')

    def imageview(self):
        return mark_safe(
                        '<a href="%s" >'
                        '<img src="%s" width="80" height="80" />'
                        '</a>' % (self.image.url, self.image.url)
                    )
        return "No Image" 
    
    
    
    
    
    

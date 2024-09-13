
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',home_view,name='home'),
    path('gallery',gallery_view,name='gallery'),
    path('category_gallery/<int:id>',category_image_view,name="category_gallery"),
    path('contact',contact_view,name='contact'),
    path('services',service_view,name='services'),
    path('about',about_view,name='about'),
    path('enquiry',enquiry_submit_view,name='enquiry'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')



  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
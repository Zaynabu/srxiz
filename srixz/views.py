from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def staff_check(user):
    return user.is_staff

def home_view(request):
    category=Category.objects.filter(
    gallery__in=Gallery.objects.filter(
        galleryimage__isnull=False
    ).distinct()
).distinct()
    banner=Banner.objects.all()
    return render(request,'index.html',{'category':category,'banner':banner,'show_footer': True})

def gallery_view(request):
    gallery=Galleryimage.objects.filter(show_in_gallery=True)
    return render(request,'gallery.html',{'gallery':gallery,'show_footer': True})


def category_image_view(request,id):
    category=Category.objects.get(id=id)
    g=Gallery.objects.filter(category=category)
    galley=Galleryimage.objects.filter(gallery__in=g)
    return render(request,'category_image.html',{'gallery':galley,'category':category,'show_footer': True})


def contact_view(request):
    form=Enquiryform()
    contact=Contact.objects.all()
    return render(request,'contact.html',{'contact':contact,'form':form,'show_footer': True})



def about_view(request):
    contact=Contact.objects.all()
    about=About.objects.all()
    return render(request,'about.html',{'contact':contact,'about':about,'show_footer': True})


def service_view(request):
    service=Service.objects.all()
    contact=Contact.objects.all()
    return render(request,'services.html',{'service':service,'contact':contact,'show_footer': True})


def enquiry_submit_view(request):
    if request.method=='POST':
        form=Enquiryform(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['firstname']
            lname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']

            Enquiry.objects.create(firstname=fname,lastname=lname,email=email,subject=subject,message=message)
            adminemail=Contact.objects.first().email
            admin_email = adminemail  # Replace with your admin email
            email_subject = f"New enquiry from {fname} {lname}"
            email_body = f"""
            You have received a new enquiry from {fname} {lname}.

            Subject: {subject}

            Message:
            {message}

            Contact Email: {email}
            """
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
                fail_silently=False,
            )
            return redirect('contact')

    else:
        return redirect('contact')



def forgotpassword_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/admin/')
        else:
            return HttpResponse("You are authenticated but not a staff member.")
    if request.method=='POST':
        form=forgotpasswordform(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            try:
                user=User.objects.get(email=email)
                print(user)
                return redirect('resetpassword')
            except:
                messages.error(request, f'Invalid email , No user found for " {email} "  ')
                return redirect(f'{reverse("forgotpassword")}')

        return render(request,'forgotpassword.html',{'form':form})
    else:
        form=forgotpasswordform()
        return render(request,'forgotpassword.html',{'form':form})



def resetpassword_view(request):
    return render(request,'passwordreset.html')
from django import forms

class Enquiryform(forms.Form):
    firstname=forms.CharField(label='Firstname',max_length=200,required=True)
    lastname=forms.CharField(label='Lastname',max_length=200,required=True)
    email=forms.EmailField(label='Email',required=True)
    subject=forms.CharField(label='Subject',max_length=200,required=True)
    message=forms.CharField(label='Message',widget=forms.Textarea,required=True)



class forgotpasswordform(forms.Form):
    email=forms.EmailField()
    

class verifyotpform(forms.Form):
    otp=forms.CharField(max_length=10)


class passwordresetform(forms.Form):
    password1=forms.CharField(max_length=10)
    password2=forms.CharField(max_length=10)
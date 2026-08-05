from django import forms
from apptest.models import Contact, Newsletter
from captcha.fields import CaptchaField
from blog.models import Comment

class FirstForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=255)
    subject = forms.CharField(label="Your Subject", max_length=255)
    email = forms.EmailField(label="Your Email", max_length=255)
    message = forms.CharField(widget=forms.Textarea, label="Your Message")


class ContactForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = "__all__"

class NewsletterForm(forms.ModelForm):
    class Meta :
        model = Newsletter
        fields = "__all__" 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']
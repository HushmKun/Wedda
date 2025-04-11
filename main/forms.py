from django import forms
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging
import time
import threading
from .models import contact

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write a message.'}))


    def send_email(self):
        thread = threading.Thread(
            target=send_contact_email,
            args=(dict(self.cleaned_data),),
        )
        thread.start()
        contact.objects.create(
            name = self.cleaned_data.get('name'),
            phone = self.cleaned_data.get('phone'),
            email = self.cleaned_data.get('email'),
            subject = self.cleaned_data.get('subject'),
            message = self.cleaned_data.get('message'),
        )
        time.sleep(3)


def send_contact_email(cleaned_data:dict):
    try:
        context = {
            "user": cleaned_data,
        }

        subject = f"{cleaned_data.get('name')} يتواصل معك."
        from_email = "info@wedda.agency"
        to = ["hussein.mukhtar@wedda.agency", "mahmoud.mamdouh@wedda.agency"]

        # Skip the .txt file for now
        html_content = render_to_string("emails/main.html", context)

        msg = EmailMultiAlternatives(subject, "", from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        logger.error(f"Sent email successfully.")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
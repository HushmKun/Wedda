from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class newsletter(models.Model):

    email= models.EmailField(_("Email"), max_length=254)    
    creation_date = models.DateTimeField(_("Creation Date"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("newsletter")
        verbose_name_plural = _("newsletters")

    def __str__(self):
        return self.email


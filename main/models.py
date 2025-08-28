from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
import os 

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'Services/Images'
    name, ext = filename.split('.')
    
    filename = instance.name + '.' + ext
    return os.path.join(upload_to, filename)

class Icon(models.Model):
    name = models.CharField(_("Icon Name"), max_length=50)
    icon_class = models.CharField(_("Icon Class"), max_length=50)

    def __str__(self):
        return self.name

class contact(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    phone = models.CharField(_("Phone Number"), max_length=50)
    email= models.EmailField(_("Email"), max_length=254)    
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Message"))

    creation_date = models.DateTimeField(_("Creation Date"), auto_now=False, auto_now_add=True)
    contacted = models.BooleanField(_("Contacted yet"), default=False)


    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return self.email

class Service(models.Model):

    name = models.CharField(_('Name'), max_length=254)
    img = models.ImageField(_("Image"), upload_to=path_and_rename)    
    excerpt = models.TextField(_("Excerpt"))
    icon = models.ForeignKey("Icon", verbose_name=_("icon"), on_delete=models.CASCADE)
    paragraph_1 = models.TextField(_("Main Paragragh"))
    paragraph_2 = models.TextField(_("Sub Paragragh"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("single_service", kwargs={"pk": self.pk})

class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    arabic_name = models.CharField(_('Arabic Name'), max_length=50)
    slug = models.SlugField(_("Slug"))
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

class Project(models.Model):

    name = models.CharField(_('Name'), max_length=254)
    thumb = models.ImageField(_("Thumbnail"), upload_to="projects/thumbnail/")    
    img = models.ImageField(_("Image"), upload_to="projects/images/")    
    category = models.ForeignKey(Tag, related_name="main_tag", on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, verbose_name=_("tags"))
    client = models.CharField(_("Client"), max_length=50)
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)
    paragraph_1 = models.TextField(_("Main Paragragh"))
    paragraph_2 = models.TextField(_("Sub Paragragh"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("single_project", kwargs={"pk": self.pk})
        
class ProjectImage(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("Image"), upload_to="projects/images/")

    class Meta:
        verbose_name = _("Project_Image")
        verbose_name_plural = _("Project_Images")

    def __str__(self):
        return self.project.name 


class Testmonial(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    position = models.CharField(_("Position"), max_length=50)
    text = models.TextField(_("Text"))
    image = models.ImageField(_("Image"), upload_to="testmonials/", blank=True, default="default.png")

    class Meta:
        verbose_name = _("Testmonial")
        verbose_name_plural = _("Testmonials")

    def __str__(self):
        return self.name


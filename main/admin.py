from django.contrib import admin

from .models import ProjectImage, contact, Service, Icon, Tag, Project, Testmonial


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ("email","creation_date", "contacted",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name","excerpt",)

@admin.register(Icon)
class IconsAdmin(admin.ModelAdmin):
    list_display = ("name","icon_class",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name","arabic_name",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image",)

@admin.register(Testmonial)
class TestmonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position",)
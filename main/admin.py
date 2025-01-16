from django.contrib import admin

from .models import newsletter


@admin.register(newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    # fields = ("email","created_at",)
    list_display = ("email","creation_date",)

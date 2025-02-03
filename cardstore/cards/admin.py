from django.contrib import admin

# Register your models here.
from .models import Card

# registering the card to the admin site
admin.site.register(Card)
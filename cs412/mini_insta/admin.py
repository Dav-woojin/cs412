#David Chung, dwjchung@bu.edu
#in our admin file, we register our profile model for use in the admin webpage

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)

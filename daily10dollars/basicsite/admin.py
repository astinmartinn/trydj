from django.contrib import admin

# Register your models here.
from .models import Gmail,Facebook
admin.site.register(Gmail)
admin.site.register(Facebook)
from django.contrib import admin
from childmissingapp . models import complainant, user,  Police
# Register your models here.

admin.site.register(complainant)
admin.site.register(user)
admin.site.register(Police)
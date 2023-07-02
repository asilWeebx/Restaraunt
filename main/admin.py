from django.contrib import admin

# Register your models here.
from .models import *
from users.models import *
admin.site.register(Categoriya)
admin.site.register(User)
admin.site.register(Menyu)
# admin.site.register(Tadbir)
admin.site.register(Bron)
admin.site.register(Chefs)
admin.site.register(Galery)
admin.site.register(Contact)
admin.site.register(Specials)
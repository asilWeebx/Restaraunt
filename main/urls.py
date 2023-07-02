from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name= "index"),
    path('accounts/profile/',index,name= "index"),
    path('create_product/',create_product,name= "create_product")
]
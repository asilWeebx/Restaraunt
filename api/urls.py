from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.categoriya import CategoryAPIView
from api.views.chefs import ChefsAPIView
from api.views.contact import ContactCreateAPIView,ContactDestroyAPIView
from api.views.menyu import MenyuAPIView
from api.views.bron import BronAPIView
from api.views.specials import SpecialsAPIView

router = DefaultRouter()
router.register('product', MenyuAPIView)
router.register('category', CategoryAPIView)
router.register('Bron', BronAPIView)
router.register('Specials', SpecialsAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactCreateAPIView.as_view()),
    path('contact/<int:pk>/', ContactDestroyAPIView.as_view())
]
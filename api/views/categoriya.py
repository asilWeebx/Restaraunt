from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from main.models import Categoriya
from api.serializer.categoriya import *

class CategoryAPIView(ModelViewSet):
    queryset = Categoriya.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCategoriyaModelSerializer,
            'create': CreateCategoriyaModelSerializer,
            'Retrieve':DetailCategoryModelSerializer,
            'update':UpdateCategoryModelSerializer,
            'partial': PartialCategoryProductModelSerializer,
            'destroy':DestroyCategoryModelSerializer
        }
        return serializer_dict.get(self.action, CategoryModelSerializer)
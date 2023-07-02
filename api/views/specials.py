from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.models import Menyu
from api.serializer.specials import *


class SpecialsAPIView(ModelViewSet):
    queryset = Specials.objects.order_by('pk')
    serializer_class = SpecialsModelSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    def get_serializer_class(self):
        serializer_dict = {
            'list':ListSpecialsModelSerializer,
            'create':CreateSpecialsModelSerializer,
            'Retrieve':DetailSpecialsModelSerializer,
            'update':UpdateSpecialsModelSerializer,
            'partial':PartialSpecialsProductModelSerializer,
            'destroy':DestroySpecialsModelSerializer
        }
        return serializer_dict.get(self.action, SpecialsModelSerializer)
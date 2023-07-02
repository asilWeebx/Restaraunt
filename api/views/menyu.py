from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.models import Menyu
from api.serializer.menyu import *


class MenyuAPIView(ModelViewSet):
    queryset = Menyu.objects.order_by('pk')
    serializer_class = MenyuModelSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    def get_serializer_class(self):
        serializer_dict = {
            'list':ListMenyuModelSerializer,
            'create':CreateMenyuModelSerializer,
            'Retrieve':DetailMenyuModelSerializer,
            'update':UpdateMenyuModelSerializer,
            'partial':PartialMenyuProductModelSerializer,
            'destroy':DestroyMenyuModelSerializer
        }
        return serializer_dict.get(self.action, MenyuModelSerializer)
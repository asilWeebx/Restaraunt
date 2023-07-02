from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.models import Bron
from api.serializer.bron import *


class BronAPIView(ModelViewSet):
    queryset = Bron.objects.all()
    serializer_class = BronModelSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]


    def get_serializer_class(self):
        serializer_dict = {
            'list':ListBronModelSerializer,
            'create':CreateBronModelSerializer,
            'Retrieve':DestroyBronModelSerializer,
            'update':UpdateBronModelSerializer,
            'partial':PartialUpdateBronModelSerializer,
            'destroy':DestroyBronModelSerializer
        }
        return serializer_dict.get(self.action, BronModelSerializer)
from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from main.models import  Chefs
from api.serializer.chefs import *


class ChefsAPIView(ModelViewSet):
    queryset = Chefs.objects.order_by('pk')
    serializer_class = ChefsModelSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def get_serializer_class(self):
        serializer_dict = {
            'list':ListChefsModelSerializer,
            'create':CreateChefsModelSerializer,
            'Retrieve':DetailChefsModelSerializer,
            'update':UpdateChefsModelSerializer,
            'destroy':DetailChefsModelSerializer
        }
        return serializer_dict.get(self.action, ChefsModelSerializer)
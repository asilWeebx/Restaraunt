from django.db.models import TextField
from rest_framework.fields import CharField, ImageField, FloatField
from rest_framework.serializers import ModelSerializer

from main.models import Chefs


class ChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        fields = '__all__'


# LIST
class ListChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        fields = '__all__'


# Create
class CreateChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        exclude = ()


# DETAIL
class DetailChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        exclude = ()


# UPDATE
class UpdateChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        exclude = ()

# DELETE
class DeleteChefsModelSerializer(ModelSerializer):
    class Meta:
        model = Chefs
        exclude= ()
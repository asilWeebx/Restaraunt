from django.db.models import TextField
from rest_framework.fields import CharField, ImageField, FloatField
from rest_framework.serializers import ModelSerializer

from main.models import Menyu


class MenyuModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        fields = '__all__'


# LIST
class ListMenyuModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        fields = ('id', 'name', 'img', 'text', 'price')

# Create
class CreateMenyuModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        exclude = ()


# DETAIL
class DetailMenyuModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        exclude = ()


# UPDATE
class UpdateMenyuModelSerializer(ModelSerializer):
    class Meta:
        model = Menyu
        exclude = ()


# PARTIAL_UPDATE
class PartialMenyuProductModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        exclude = ()


# DELETE
class DestroyMenyuModelSerializer(ModelSerializer):

    class Meta:
        model = Menyu
        exclude = ()

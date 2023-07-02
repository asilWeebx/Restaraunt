from django.db.models import TextField
from rest_framework.fields import CharField, ImageField, FloatField
from rest_framework.serializers import ModelSerializer

from main.models import Specials


class SpecialsModelSerializer(ModelSerializer):

    class Meta:
        model = Specials
        fields = '__all__'


# LIST
class ListSpecialsModelSerializer(ModelSerializer):

    class Meta:
        model = Specials
        fields = ('id', 'name', 'newname', 'text', 'img')

# Create
class CreateSpecialsModelSerializer(ModelSerializer):

    class Meta:
        model = Specials
        exclude = ()


# DETAIL
class DetailSpecialsModelSerializer(ModelSerializer):

    class Meta:
        model = Specials
        exclude = ()


# UPDATE
class UpdateSpecialsModelSerializer(ModelSerializer):
    class Meta:
        model = Specials
        exclude = ()


# PARTIAL_UPDATE
class PartialSpecialsProductModelSerializer(ModelSerializer):
    class Meta:
        model = Specials
        exclude = ()


# DELETE
class DestroySpecialsModelSerializer(ModelSerializer):

    class Meta:
        model = Specials
        exclude = ()

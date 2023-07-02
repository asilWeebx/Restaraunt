from rest_framework.fields import CharField, HiddenField
from rest_framework.routers import DefaultRouter
from rest_framework.serializers import ModelSerializer

from main.models import Bron


class BronModelSerializer(ModelSerializer):

    class Meta:
        model = Bron
        fields = '__all__'



# LIST
class ListBronModelSerializer(ModelSerializer):

    class Meta:
        model = Bron
        exclude = ()

# Create
class CreateBronModelSerializer(ModelSerializer):
    user = HiddenField(default=DefaultRouter())

    class Meta:
        model = Bron
        exclude = ()


# DETAIL
class DetailBronModelSerializer(ModelSerializer):

    class Meta:
        model = Bron
        exclude = ()


# UPDATE
class UpdateBronModelSerializer(ModelSerializer):
    user = HiddenField(default=DefaultRouter())

    class Meta:
        model = Bron
        exclude = ()


# PARTIAL_UPDATE
class PartialUpdateBronModelSerializer(ModelSerializer):
    user = HiddenField(default=DefaultRouter())

    class Meta:
        model = Bron
        exclude = ()


# DELETE
class DestroyBronModelSerializer(ModelSerializer):

    class Meta:
        model = Bron
        exclude = ()
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from main.models import Categoriya


class CategoryModelSerializer(ModelSerializer):

    def validate(self, data):
        if Categoriya.objects.filter(name=data['name']).exists():
            raise ValidationError('This category title already exists')
        return data

    class Meta:
        model = Categoriya
        fields = '__all__'
# LIST
class ListCategoriyaModelSerializer(ModelSerializer):

    class Meta:
        model = Categoriya
        fields = ('id', 'name')

# Create
class CreateCategoriyaModelSerializer(ModelSerializer):

    class Meta:
        model = Categoriya
        exclude = ()

# PARTIAL_UPDATE
class PartialCategoryProductModelSerializer(ModelSerializer):
    class Meta:
        model = Categoriya
        exclude = ()


class DestroyCategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Categoriya
        exclude = ()

# UPDATE
class UpdateCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Categoriya
        exclude = ()

# DETAIL
class DetailCategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Categoriya
        exclude = ()

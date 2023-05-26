from rest_framework.serializers import ModelSerializer
from .models import *

class ImagensAtelierSerializer(ModelSerializer):
    class Meta:
        model = ImagensAtelier
        fields = ["id", "imagem", "desc_imagem"]

    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()

        return instance

from rest_framework import serializers
from .models import student

class studenserializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name','age']
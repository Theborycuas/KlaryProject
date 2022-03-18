from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


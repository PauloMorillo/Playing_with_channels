from rest_framework import serializers

from .models import User, Help, Store

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('first_name', 'telefono', 'edad', 'description')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'plaza', 'tel', 'cel', 'city', 'description')


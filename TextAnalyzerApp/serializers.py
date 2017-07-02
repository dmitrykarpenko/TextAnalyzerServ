from rest_framework import serializers

from .models import User, UserText


class UserTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserText
        #fields = ('title', 'text')
        exclude = ()


class UserSerializer(serializers.ModelSerializer):
    cards = UserTextSerializer(read_only=True, many=True)

    class Meta:
        model = User
        #fields = ('name')
        exclude = ()

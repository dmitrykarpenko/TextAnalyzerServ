from rest_framework import serializers

from .models import User, UserText

all_fields = '__all__'

class UserTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserText
        fields = all_fields
        #exclude = ()


class UserSerializer(serializers.ModelSerializer):
    texts = UserTextSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = all_fields
        #exclude = ('id',)

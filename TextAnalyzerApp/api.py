from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer, UserTextSerializer
from .models import User, UserText

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTextViewSet(ModelViewSet):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer

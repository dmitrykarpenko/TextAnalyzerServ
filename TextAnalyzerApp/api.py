from rest_framework.generics import ListAPIView

from .serializers import UserSerializer, UserTextSerializer
from .models import User, UserText

class UserApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTextApi(ListAPIView):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer

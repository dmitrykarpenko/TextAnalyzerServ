from rest_framework.routers import DefaultRouter

from .api import UserViewSet, UserTextViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'usertexts', UserTextViewSet)

urlpatterns = router.urls

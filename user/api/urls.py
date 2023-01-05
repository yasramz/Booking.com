from user.api.views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('login/step-one/', LoginStepOneAPIView.as_view(), name="step_one"),
    path('login/step-two/', LoginStepTwoAPIView.as_view(), name="step_two")
]
urlpatterns += router.urls

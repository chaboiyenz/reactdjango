from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('signup/', register_user, name='signup'),
    path('', include(router.urls)),
]

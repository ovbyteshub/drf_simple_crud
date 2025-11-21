from rest_framework import routers
from .api import ProjectViewSet

routers = routers.DefaultRouter()

routers.register('api/projects', ProjectViewSet, basename='project')

urlpatterns = routers.urls
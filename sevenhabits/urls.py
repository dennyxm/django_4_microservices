from django.conf.urls import url
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from sevenhabits.views import RolesViewSet, GoalsViewSet

schemaview = get_swagger_view(title='Seven Habit API')

router = routers.DefaultRouter()

router.register('roles', RolesViewSet)
router.register('goals', GoalsViewSet)

urlpatterns =[
    url('docs/', schemaview)
]
urlpatterns += router.urls
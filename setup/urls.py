from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet, CurseViewSet, RegistrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('curses', CurseViewSet, basename='Curses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]

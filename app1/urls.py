from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
#
from app1 import views


router=DefaultRouter()
router.register('Register/',views.User_Register),
# router.register('Login/',views.Login_user),
router.register('Task/',views.Creat_task)


urlpatterns=[
    re_path(r'',include(router.urls))

]
# urlpatterns=[
#     re_path(r'Register/',views.User_Register),
#     re_path(r'Task/',views.Creat_task),
# ]


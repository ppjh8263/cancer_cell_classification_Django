from django.conf.urls import url
from .views import RegisterUser

urlpatterns = [
    url('regist_user',RegisterUser.as_view(),name='regist_user'),
]

from django.urls import path
from . import views

app_name = 'cell'

urlpatterns = [
    path('',views.index, name='index'),    # path('<int:question_id>/',

    path('image_upload',
         views.image_upload, name='image_upload'),

]

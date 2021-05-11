from django.urls import path
from . import views

app_name = 'cell'

urlpatterns = [
    path('',views.index, name='index'),

    path('image_upload',
         views.image_upload, name='image_upload'),

    path('detail/<int:cell_image_id>',
             views.detail, name='detail'),

    # path('update/<int:cell_image_id>/',
    #     views.update, name='update'),

]

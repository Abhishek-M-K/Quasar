from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="benz"),
    path('add-cam',views.add_cam,name="add-cam")
]


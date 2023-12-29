from django.urls import path
from .views import comments_list

urlpatterns = [
    path("<int:code>/<str:name>",comments_list,  name="comments_list")
]

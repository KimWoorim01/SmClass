
from django.urls import path

# from . import views,apps,models
from . import views

app_name = ''
urlpatterns = [
    # url 링크, views 함수호출
    path('',views.index, name = 'index'),
]

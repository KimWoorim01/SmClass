
from django.urls import path

# from . import views,apps,models
from . import views

app_name = 'students'
urlpatterns = [
    # url 링크, views 함수호출
    path('write/', views.write, name='write'),
    path('list/', views.list, name='list'),
    path('view/', views.view, name='view')
]

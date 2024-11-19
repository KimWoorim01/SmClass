from django.urls import path,include
from . import views
app_name='students'   ## name:url시 사용
urlpatterns = [
    path('write/',views.write,name='write1' ), # 학생입력페이지
]

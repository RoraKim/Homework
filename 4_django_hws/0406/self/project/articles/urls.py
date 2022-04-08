from django.urls import path
#django는 명시적으로 경로를 표시한다 
from . import views

#app name 역시 설정해줬었다 
app_name = 'articles'

urlpatterns = [
    #path_name 설정해줘야한다
    #물론 필수는 아님 
    #빈 문자열처럼 보이지만 앞에 root/articles/뒤의 경로를 의미함
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]

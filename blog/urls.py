from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    path('info/', views.PostList.as_view(), name='info'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    url(r'^service/$', views.service, name='service'),
    url(r'^contact/$', views.contact, name='contact'),
    url('create/', views.PostCreate.as_view(), name='create'),
]

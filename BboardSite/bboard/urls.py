from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    re_path(r'^bboard/(?P<slug>[-\w]+)/$', views.detail, name='detail'),
    re_path(r'^bboard/(?P<slug>[-\w]+)/delete/$', views.delete, name='delete'),
]
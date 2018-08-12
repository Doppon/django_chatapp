from django.urls import path

from . import views


urlpatterns = [
    # 元のコードは→url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    # 元コードは→url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('<slug:room_name>/', views.room, name='room'),
]

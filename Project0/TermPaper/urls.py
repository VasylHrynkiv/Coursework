from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('dev', views.dev, name = 'dev'),
    path('pack', views.pack, name = 'pack'),
    path('adddata', views.adddata, name = 'adddata'),
    path('adddev', views.adddev, name = 'adddev'),
    path('addpack', views.addpack, name = 'addpack'),
    path('update/<int:pk>', views.update, name = 'update'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
    path('deldev/<int:pk>', views.deldev, name = 'deldev'),
    path('delpack/<int:pk>', views.delpack, name = 'delpack'),
    path('search', views.search, name = 'search'),
]
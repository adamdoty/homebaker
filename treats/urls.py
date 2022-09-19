from django.urls import path, include

from . import views

app_name = 'treats'
urlpatterns = [
    path('', views.treat_list, name='treat_list'),
    path('<int:pk>', views.treat_detail, name='treat_detail'),
    path('new/', views.treat_new, name='treat_new'),
    path('edit/<int:pk>', views.treat_edit, name='treat_edit'),
    path('delete/<int:pk>', views.treat_delete, name='treat_delete')
]
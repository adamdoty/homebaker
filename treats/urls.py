from django.urls import path, include

from . import views

app_name = 'treats'
urlpatterns = [
    path('', views.treat_list, name='treat_list'),  # change to treat-catalogue later, empty for convenience
    path('treat/<int:pk>', views.treat_detail, name='treat_detail'),
    path('new-treat/', views.treat_new, name='treat_new'),
    path('edit/<int:pk>', views.treat_edit, name='treat_edit'),
    path('delete/<int:pk>', views.treat_delete, name='treat_delete'),
    path('treat/<int:pk>/note', views.treat_note, name='treat_note'),
    path('edit/<int:pk>/note', views.treat_note_edit, name='treat_note_edit'),
    path('delete/<int:pk>/note', views.treat_note_delete, name='treat_note_delete'),
    path('treat-request', views.treat_request, name='treat_request'),
    path('coupon-tracker', views.coupon_tracker, name='coupon_tracker'),
    path('coupon/<int:pk>', views.coupon_detail, name='coupon_detail'),
    path('new-coupon/', views.coupon_new, name='coupon_new'),
    path('edit/<int:pk>coupon', views.coupon_edit, name='coupon_edit'),
    path('delete/<int:pk>/coupon', views.coupon_edit, name='coupon_delete'),
    path('register', views.register, name='register'),
    path('my-coupons', views.my_coupons, name='my_coupons'),
]

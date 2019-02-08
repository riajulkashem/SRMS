from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('find-result/', views.find_result_view, name='find_result'),
    path('change-password/', views.PasswordChangeView.as_view(), name='change_password'),
    path('find-result/<int:pk>/result/', views.result, name='get_result'),
]

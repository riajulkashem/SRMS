from django.urls import path
from student_classes.views import *

app_name = 'student_classes'

urlpatterns = [
    path('create/', StudentClassCreateView.as_view(), name='create_class'),
    path('update/<int:pk>/', StudentClassUpdateView.as_view(), name='update_class'),
    path('delete/<int:pk>/', StudentClassDeleteView.as_view(), name='delete_class'),
    path('list/', StudentClassListView.as_view(), name='class_list'),
]
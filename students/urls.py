from django.urls import path

from students.views import (
    StudentCreateView, StudentListView, StudentUpdateView, StudentDeleteView
)


app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete'),
]
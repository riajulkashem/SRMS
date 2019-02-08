from django.urls import path
from .views import (
    SubjectCreateView, SubjectListView, SubjectUpdateView, SubjectDeleteView,
    SubjectCombinationCreateView, SubjectCombinationListView, SubjectCombinationUpdateView, SubjectCombinationDeleteView
)

app_name = 'subjects'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('create/', SubjectCreateView.as_view(), name='create_subject'),
    path('update/<int:pk>/', SubjectUpdateView.as_view(), name='update_subject'),
    path('delete/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),

    # SubjectConbinations
    path('combination/create/', SubjectCombinationCreateView.as_view(), name='create_subject_combination' ),
    path('combination/list/', SubjectCombinationListView.as_view(), name='subject_combination_list' ),
    path('combination/update/<int:pk>', SubjectCombinationUpdateView.as_view(), name='subject_combination_update' ),
    path('combination/delete/<int:pk>', SubjectCombinationDeleteView.as_view(), name='subject_combination_delete' ),
]
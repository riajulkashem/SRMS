from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import StudentClass
from .forms import StudentClassForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class StudentClassCreateView(LoginRequiredMixin, CreateView):
    model = StudentClass
    form_class = StudentClassForm

    
    def get_context_data(self, **kwargs):
        context = super(StudentClassCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Add Student Class'
        context['panel_name'] = 'Classes'
        context['panel_title'] = 'Add Class'
        return context

class StudentClassListView(LoginRequiredMixin, ListView):
    model = StudentClass

    field_list = [
        'Class Name', 'Class Name In Numeric', 'Section', 'Creation Date'
    ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Classes'
        context['panel_name']   =   'Classes'
        context['panel_title']  =   'View Classes Info'
        context['field_list']   =   self.field_list
        return context

class StudentClassUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentClass
    form_class = StudentClassForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('student_classes:class_list')

class StudentClassDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentClass
    template_name_suffix = '_delete'
    success_url = reverse_lazy('student_classes:class_list')

    def get_context_data(self, **kwargs):
        context = super(StudentClassDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Class Delete Confirmation'
        context['panel_name'] = 'Classes'
        context['panel_title'] = 'Delete Class'
        return context

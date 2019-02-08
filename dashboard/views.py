from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from results.models import DeclareResult
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core import serializers
import json

from student_classes.models import StudentClass
from results.models import DeclareResult
from subjects.models import Subject
from students.models import Student


def index(request):
    print('Inside Home Page')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ",username)
        print("Password = ",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            context = {'message':'Invalid User Name and Password'}
            return render(request, 'index.html', context)
    return render(request, 'index.html', {'name': 'Riajul Kashem', 'pass': 'login@srms'})


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

    
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['cls'] = StudentClass.objects.count()
        context['results'] = DeclareResult.objects.count()
        context['students'] = Student.objects.count()
        context['subjects'] = Subject.objects.count()
        return context
    

def find_result_view(request):
    student_class = DeclareResult.objects.all()
    if request.method == "POST":
        print("\nRequested From Post Data\n")
        data = request.POST
        print(data)
        # data = json.loads(form)
        roll = int(data['rollid'])
        pk = int(data['class'])
        clss = get_object_or_404(DeclareResult, pk=pk)
        if clss.select_student.student_roll == roll:
            print("\nMached POST Data\n")
            data = {
                'pk': data['class']
            }
            return JsonResponse(data)
        else:
            pk = '0'
            data = {
                'pk': pk
            }
            return JsonResponse(data)
    return render(request, 'find_result.html', {'class':student_class})

def result(request, pk):
    r = get_object_or_404(DeclareResult, pk=pk)
    return render(request, 'result.html', {'object':r, 'pk':pk})


class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard:dashboard')
    template_name = 'password_change_form.html'

    
    def get_context_data(self, **kwargs):
        context = super(PasswordChangeView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Admin Change Password'
        context['panel_title'] = 'Admin Change Password'
        return context
    
    

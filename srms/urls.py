from dashboard import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('results/', include('results.urls')),
    path('subjects/', include('subjects.urls')),
    path('students/', include('students.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('classes/', include('student_classes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

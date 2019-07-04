"""REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from emp import views
from emp.views import EmployeeList, EmployeePost, EmployeeCreateAPIView,EmployeeUpdateAPIView,ExampleAllView

urlpatterns = [
    #adminurl http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    #post http://localhost:8000/employees/
    url(r'^employees/$', EmployeePost.as_view()),
    url(r'^employees/(?P<emp_id>\d+)/$', EmployeeList.as_view()),
    #url(r'^employees/operations/$', EmployeeAPIView.as_view())
    #http://localhost:8000/emp/ -> GET ALL
    #http://localhost:8000/emp/?q=1 -> GET based on id
    url(r'^emp/$', EmployeeCreateAPIView.as_view()),
    #Not bale to PUT in this as it says emp_id already exists if we try to update
    url(r'^emp_update/$',EmployeeUpdateAPIView.as_view()),
    #http://localhost:8000/emp_all/1/ -> GET, PUT, PATCH, DELETE
    url(r'^emp_all/(?P<pk>\d+)/$', ExampleAllView.as_view()),
]

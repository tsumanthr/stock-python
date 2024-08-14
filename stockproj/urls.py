"""stockproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from stockapp.views import login_page, stockentryuser_page,report_page,stockentrymanager_page,showreport_page,returnstockmanger_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('stockentry', stockentryuser_page, name='stockentryuser'),
    path('report', report_page, name='report'),
    path('manager2nd', stockentrymanager_page, name='stockentrymanager'),
    path('reportshow', showreport_page, name='showreport'),
    path('rstockmanger', returnstockmanger_page, name='returnstockmanger'),
]

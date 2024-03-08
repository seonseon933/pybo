"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), #URL을 자동 정규화하기 떄문에 / 붙임.
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), # settings의 '/'에 해당됨.
]
handler404 = 'common.views.page_not_found'
# 오류 발생 시 사용자가 정의한 뷰 함수가 호출됨. 
# handler404 변수는 반드시 config/urls.py에 등록해야 함.
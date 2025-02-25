"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from sspApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'), # 메인화면
    path('join_01/', views.join_01, name='join_01'), # 회원가입화면
    path('join_02/', views.join_02, name='join_02'), # 회원가입화면
    path("check-business-number/", views.check_business_number, name="check_business_number"), # 사업자등록번호 유무 조회
]

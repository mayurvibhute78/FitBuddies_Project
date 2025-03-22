"""
URL configuration for FitBuddies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from fitapp.models import Customer
from fitapp.views import CustomerCreate, CustomerList,CustomerUpdate,CustomerDelete, CustomerDetail
from fitapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index' ),
    path("features",views.features, name='feature'),
    path("diet_plan",views.diet_plan, name='diet_plan'),
    path("contact_us",views.contact, name='contact'),
    path("male_workout",views.maleworkout, name='maleworkout'),
    path("female_workout",views.femaleworkout, name='femaleworkout'),
    path("pt_info",views.pt_info, name='pt_info'),
    path("pt_gym",views.pt_gym, name='pt_gym'),
    path("pt_online",views.pt_online, name='pt_online'),
    path("pt",views.pt, name='pt'),
    path("mchest",views.mchest, name='mchest'),
    path("mback",views.mback, name='mback'),
    path("marms",views.marms, name='marms'),
    path("mshoulder",views.mshoulder, name='mshoulder'),
    path("mabs",views.mabs, name='mabs'),
    path("mlegs",views.mlegs, name='mlegs'),
    path("fchest",views.fchest, name='fchest'),
    path("fback",views.fback, name='fback'),
    path("farms",views.farms, name='farms'),
    path("fshoulder",views.fshoulder, name='fshoulder'),
    path("fabs",views.fabs, name='fabs'),
    path("flegs",views.flegs, name='flegs'),

    path("create/", CustomerCreate.as_view(), name='create'),
    path("list/",CustomerList.as_view(), name='list' ),
    path("update/<pk>",CustomerUpdate.as_view(), name='update'),
    path("delete/<pk>",CustomerDelete.as_view(), name='delete'),
    path("detail/<pk>",CustomerDetail.as_view(), name='detail'),    
]

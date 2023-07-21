"""city360 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index),
    path('userreg',views.userreg),
    path('addseller',views.addseller),
    path('adduser',views.adduser),
    path('login',views.login),
    path('addlogin',views.addlogin),
    path('logout/',views.logout),
    path('viewusers',views.viewusers),
    path('v_book',views.v_book),
    path('wdelete/<int:id>',views.wdelete,name="wdelete"),
    path('udelete/<int:id>',views.udelete,name="udelete"),
    path('check_out',views.check_out),
    path('viewworker',views.viewworker),
    path('viewsellers',views.viewsellers),
    path('viewbooking',views.viewbooking),
    path('uapprove/<int:id>',views.uapprove,name="uapprove"),
    path('wapprove/<int:id>',views.wapprove,name="wapprove"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('confirm/<int:id>',views.confirm,name="confirm"),
    path('reject/<int:id>',views.reject,name="reject"),
    path('addbook',views.addbook),
    path('cancel/<int:id>',views.cancel),
    path('viewwrker/<str:wid>',views.viewwrker),
    path('uprofile',views.uprofile),
    path('wprofile',views.wprofile),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

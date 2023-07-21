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
    path('v_payments',views.v_payments),
    path('v_book',views.v_book),
    path('v_payment',views.v_payment),
    path('bid/<int:id>',views.bid),
    path('v_sellerfeed',views.v_sellerfeed),
    path('v_userfeed',views.v_userfeed),
    path('check_out',views.check_out),
    path('v_auction',views.v_auction),
    path('bid/ad_auction',views.ad_auction),
    path('viewworker',views.viewworker),
    path('load_bid/<int:id>',views.load_bid,name="load_bid"),
    path('load_bid/update/<int:id>',views.update,name="update"),
    path('return_pro/addreturn/<int:id>',views.addreturn,name="addreturn"),
    path('v_product',views.v_product),
    path('viewsellers',views.viewsellers),
    path('viewbooking',views.viewbooking),
    path('uapprove/<int:id>',views.uapprove,name="uapprove"),
    path('wapprove/<int:id>',views.wapprove,name="wapprove"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('confirm/<int:id>',views.confirm,name="confirm"),
    path('reject/<int:id>',views.reject,name="reject"),
    path('addbook',views.addbook),
    path('u_feeback',views.u_feeback),
    path('s_feeback',views.s_feeback),
    path('payments/add_payment/<int:id>',views.add_payment),
    path('payments/<int:id>',views.payments),
    path('udelete/<int:id>',views.udelete),
    path('return_pro/<int:id>',views.return_pro),
    path('wdelete/<int:id>',views.wdelete),
    path('cdelete/<int:id>',views.cdelete),
    path('cancel/<int:id>',views.cancel),
    path('viewwrker/<str:item_name>',views.viewwrker),
     path('viewrating/<str:item_name>/', views.viewrating, name='viewrating'),
    path('uprofile',views.uprofile),
    path('wprofile',views.wprofile),
    path('v_return',views.v_return),
    path('view_mypro',views.view_mypro),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    path('rating/<int:id>',views.rating),
    path('buyaucpro/<int:id>',views.buyaucpro),
    path('buyaucpro/add_aucpayment/<int:id>',views.add_aucpayment),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""Restaurant URL Configuration

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
from django.urls import include
from restaurant.views import registro_view
from restaurant.views import carta_view
from restaurant.views import detalle_carta_view
from restaurant.views import index_view
from restaurant.views import ingrediente_view
from restaurant.views import login_view
from restaurant.views import logout_view
from restaurant.views import mesa_view
from restaurant.views import comanda_view
from restaurant.views import detalle_comanda_view
from restaurant.views import transbankpay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carta', carta_view.index),
    path('', carta_view.index),
    path('registro/', registro_view.index),
    path('detalle_carta/', detalle_carta_view.index),
    path('home/', index_view.index),
    path('ingrediente/', ingrediente_view.index),
    path('login/', login_view.index),
    path('logout/', logout_view.index),
    path('mesa/', mesa_view.index),
    path('comanda/', comanda_view.index),
    path('detalle_comanda/', detalle_comanda_view.index),
    path('commit-pay/', transbankpay.commitpay),
    path('webpay-plus-create', transbankpay.webpay_plus_create),   
]

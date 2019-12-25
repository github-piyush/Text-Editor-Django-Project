"""textutil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),            #index is a function in views.py where Hello World is written
                                            #since it has path='' so its link will be 127.0.0.1, means there is nothing after the main link   

    path('go',views.go,name='go')
    
    
    
    
    
    
    # path('about', views.about, name='about'),        #name is basically a text written on the link to open its function ex. http/127.0.0.1:8000/about.
    #                                 #ex. http/127.0.0.1:8000/about --- this will print the output of the function views.about (i.e. a function about in views.py)
                                    
    # path('links', views.links, name='links'),

    # path('rempunc', views.rempunc, name='rempunc'),
    # path('capfirst', views.capfirst, name='capfirst'),
    # path('charcount', views.charcount, name='charcounts')

]           

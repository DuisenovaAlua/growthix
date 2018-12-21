"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import things.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Test/<user>/<root>/result/',views.result, name='res'),
    path('Test/<user>/<root>',views.Test_view,name='test'),
    path('registration1',views.Save,name="reg1"),
    path('',views.index,name='home'),
    path('registration2/<user>',views.reg2,name='reg2'),
    path('registration3/<user>',views.reg4,name='reg4'),
    path('registration4/<user>',views.reg3,name='reg3'),
    path('notAvailable/<user>',views.no,name="notAvailable")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
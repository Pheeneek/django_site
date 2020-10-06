"""test_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import sys
from datetime import datetime

from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, JsonResponse


def _get_info(request):
    # html = f"""<html><body>{sys.platform} | {sys.version}</body></html>"""
    json_ = {
        'platform': sys.platform,
        'python': sys.version
    }

    return JsonResponse(json_)


def _get_date(request):
    html = f"""{datetime.now()}"""
    return HttpResponse(html)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', _get_info),
    path('date/', _get_date),

]


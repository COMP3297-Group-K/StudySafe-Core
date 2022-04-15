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
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="StudySafe Core API",
      default_version='v1',
      description="StudySafe Core provides a RESTful API for maintaining records of the times \
          at which members of HKU enter and exit enclosed public venues such as classrooms and \
          lecture theatres on campus.",
      terms_of_service="https://github.com/COMP3297-Group-K/StudySafe/blob/main/README.md",
      contact=openapi.Contact(email="jolinc@hku.hk"),
      license=openapi.License(name=""),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Core/',include('Core.urls')),
    path('Trace/', include('Trace.urls')),
    path('Core/APIDoc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

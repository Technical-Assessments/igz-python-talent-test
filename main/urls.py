"""URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework import routers

from apps.mathapi.home_views import index, documentation
from apps.mathapi.views import (
    matrix_sum_view,
    matrix_diagonal_sum_view,
    string_encoder_view
)


urlpatterns = [
    path('', index, name='home'),
    path('index/', index),
    path('documentation/', documentation, name='docs'),

    path('api/matrix/sum/', matrix_sum_view),
    path('api/matrix/diagonal_sum/', matrix_diagonal_sum_view),
    path('api/string/encode/', string_encoder_view),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()


""" router = routers.DefaultRouter()
router.register(r'api', MatrixSumView)

urlpatterns = [
    path('', index, name='home'),
    path('index/', index),
    path('documentation/', documentation, name='docs'),

    # path('api/post/', MatrixSumView.as_view()),
    # path('api/get/', MatrixSumView.as_view()),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/', MatrixSumView),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns() """

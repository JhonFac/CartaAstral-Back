from django.urls import path

from .views import InfoAstral

urlpatterns = [
    path('infoastral/', InfoAstral.as_view(), name='info_astral'),  
]
from django.urls import path

from .views import InfoAstral, UserProfileCreateView

urlpatterns = [
    path('infoastral/', InfoAstral.as_view(), name='info_astral'),  
    path('userprofile/', UserProfileCreateView.as_view(), name='userprofile-create'),
]

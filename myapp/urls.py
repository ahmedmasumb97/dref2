from .views import ResgisterView,Protectd
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('register/',ResgisterView.as_view(),name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('protected/', Protectd.as_view(), name='protected')  
    
]

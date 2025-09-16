
from django.urls import path
from apps.usuarios.views import login,logout,cadastrar

urlpatterns = [
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cadastrar/',cadastrar,name='cadastrar'),    
]


from django.urls import path
from galeria.views import index,imagem,buscar


urlpatterns = [
    path('',index,name='index'),
    path('categoria/<str:filtro_categoria>',index,name='index_categoria'),
    path('imagem/<int:foto_id>',imagem,name='imagem'),
    path('buscar',buscar,name='buscar'),
]

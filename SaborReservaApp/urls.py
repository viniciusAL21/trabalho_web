from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('index', views.home, name='index'),
    path('salvar/', views.salvar, name='salvar'),
    path('cadastrar_vendedor/',views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path('slv_vendedor/', views.salvar_vendedor, name='slv_vendedor'),
    path('sair/', views.deslogar, name='sair'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autos/', views.lista_autos, name='autos_list'),
    path('autos/<int:auto_id>/', views.detalle_auto, name='detalle_auto'),
    path('crear_auto/', views.crear_auto, name='crear_auto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('autos/<int:auto_id>/eliminar/', views.eliminar_auto, name='eliminar_auto'), 
]

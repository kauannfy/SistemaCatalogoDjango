from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_filmes, name='lista'),
    path('detalhe/<int:id>/', views.detalhe_filme, name='detalhe'),
]
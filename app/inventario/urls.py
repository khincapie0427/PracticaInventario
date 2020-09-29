from django.urls import path
from . import views


#Cada url tiene asociada una vista, la petición se dirige a esa vista y es procesada de formas diferentes según corresponda

urlpatterns = [
    path('/', views.index, name='index'),
    path('/delete/<id>', views.delete),
    path('/edit/<id>', views.edit)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoute),
    path('persons/', views.getPersons),
    path('persons/create/', views.createPerson),
    path('persons/<int:pk>/update/', views.updatePerson),
    path('persons/<int:pk>/delete/', views.deletePerson),
    path('persons/<int:pk>/', views.getPerson),
    path('vehicles/', views.getVehicles),
    path('vehicles/<int:pk>/', views.getVehiclesByClient),
    path('vehicles/create/', views.createVehicle),
    path('vehicles/<int:pk>/update/', views.updateVehicle),
    path('vehicles/<int:pk>/delete/', views.deleteVehicle)
]
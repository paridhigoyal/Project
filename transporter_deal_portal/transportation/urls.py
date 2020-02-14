from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-vehicle/', views.add_vehicle, name='add-vehicle'),
    path('vehicles/', views.vehicle_list, name='vehicle-list'),
    path('create-deal/', views.create_deal, name='create-deal'),
    path('edit-vehicle/<int:id>', views.edit_vehicle, name ='edit-vehicle'),
    path('update-vehicle/<int:id>', views.update_vehicle,name='update-vehicle'),
    path('delete-vehicle/<int:id>', views.delete_vehicle, name='delete-vehicle'),
]

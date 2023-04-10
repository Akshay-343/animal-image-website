from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animal_list/', views.AnimalListView.as_view(), name='animal_list'),
    path('animal_detail/<int:pk>', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('animal/create/', views.AnimalCreate.as_view(), name='animal_create'),
    path('animal/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal_update'),
    path('animal/<int:pk>/delete/', views.animal_delete, name='animal_delete'),
    path('animal_images/', views.animal_image_list, name='animal_image_list'),

]

from django.urls import path
from .import views

urlpatterns = [
    path('',views.Welcome),
    path('insert/', views.Insert_emp, name='insert'),
    path('show', views.Show_emp, name='show'),
    path('edit/<int:pk>', views.Edit_emp, name='edit'),
    path('remove/<int:pk>', views.Delete_emp, name='remove')
]

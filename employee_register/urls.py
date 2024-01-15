from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee-insert'),
    path('<int:id>/', views.employee_form, name='employee-update'),
    path('list/', views.employee_list, name='employee-list'),
    path('delete/<int:id>/', views.employee_delete, name='employee-delete'),
]

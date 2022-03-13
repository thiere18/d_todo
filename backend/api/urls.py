from django.urls import path
from . import views

urlpatterns=[
    # path('', views.api_over_view, name='api_over_view'),
    path('', views.TodoMixinView.as_view(), name='task_list'),
    path('<int:pk>/', views.TodoMixinView.as_view(), name='task-detail'),






]
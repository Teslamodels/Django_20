from django.urls import path
from .views import (
    List,
    Detail,
    Create,
    Update,
    Delete
    )

urlpatterns = [
    path('', List.as_view(), name='menu'),
    path('post/<int:pk>/', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
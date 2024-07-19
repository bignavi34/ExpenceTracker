from django.urls import path
from expence import views
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<uuid>', views.delete, name='delete')
]
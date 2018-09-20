from django.urls import path
from view_table import views


urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/', views.instrumentListView.as_view(),
         name='instruments'),
    path('instrument/<int:pk>', views.instrumentDetailView.as_view(),
         name='instrument-detail'),
    path('show_table/', views.show_table, name='show_table'),
]

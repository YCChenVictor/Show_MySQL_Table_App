from django.urls import path
from Show_Table import views


urlpatterns = [
    path('', views.index, name='index'),
    path('instruments/', views.instrumentListView.as_view(),
         name='instruments'),
    path('instrument/<int:pk>', views.instrumentDetailView.as_view(),
         name='instrument-detail'),
    path('show_table/', views.instrumentListView.show_table, name='show_table'),
]

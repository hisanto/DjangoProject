from django.urls import path

# from .views import CsvDataView
from . import views

urlpatterns = [
    # path('', CsvDataView.as_view(), name = 'csv_index')
    path('', views.CsvDataListView.as_view(), name='csvdata_List'),
    path('create/', views.CsvDataCreatView.as_view(), name='csvdata_create'),
    path('detail/<int:pk>', views.CsvDataDetailView.as_view(), name='etl_csvdata_detail'),
    path('update/<int:pk>', views.CsvDataUpdateView.as_view(), name='etl_csvdata_update')
]
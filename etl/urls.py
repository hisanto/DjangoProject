from django.urls import path

# from .views import CsvDataView
from . import views

urlpatterns = [
    # path('', CsvDataView.as_view(), name = 'csv_index')
    path('', views.CsvDataListView.as_view(), name='csvdata_List')
]
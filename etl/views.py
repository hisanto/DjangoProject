from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import CsvData
# Create your views here.

#
# class CsvDataView(View):
#     template_name = 'etl/csvdata_list.html'
#
#     def get(self, request, *args, **kwargs):
#         csv_data = CsvData.objects.all()
#         return render(request,
#                       self.template_name,
#                     {"csv_data":csv_data}
#         )

#good approach
class CsvDataListView(ListView):
    model = CsvData

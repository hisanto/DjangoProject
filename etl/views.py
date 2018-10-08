from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DetailView , UpdateView
from .models import CsvData
from .forms import CsvDataForm


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

# good approach
class CsvDataListView(ListView):
    model = CsvData


# classbased view for forms
class CsvDataCreatView(CreateView):
    model = CsvData  # k sanga depend 6 bhanne
    form_class = CsvDataForm


class CsvDataDetailView(DetailView):
    model = CsvData

class CsvDataUpdateView(UpdateView):
    model = CsvData
    form_class = CsvDataForm

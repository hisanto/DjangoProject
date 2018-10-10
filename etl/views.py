import csv, json

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView , UpdateView ,DeleteView
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


class CsvDataDeleteView(DeleteView):
    model = CsvData
    #success_url = reverse_lazy('csvdata_list')

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        resp = {"delete":"OK"}
        return HttpResponse(json.dumps(resp))


def upload_process(request):
    if request.method == 'POST':
        file = request.FILES['file_input_name']
        file_data = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(file_data)
        for each in reader:
            name = each.get('name')
            ip_address = each.get('ip_address')
            mac_address = each.get('mac_address')
            CsvData.objects.create(
                name= name,
                ipv4 = ip_address,
                mac_address = mac_address
            )
        return redirect('csvdata_list')
    return render(request, template_name='etl/file_upload.html', context={})
